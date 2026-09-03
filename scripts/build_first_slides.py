#!/usr/bin/env python3
"""Convert the AEE 202 slide-derived question banks into the First Shared Slide
category: ~100 questions, spread across 5 topics, with detailed slide-based
explanations. Emits .first_slides_out.json for the splice script."""
import importlib.util
import json
import re
import sys

QDIR = "/home/user/work/qbank"

def load(name):
    spec = importlib.util.spec_from_file_location(name, f"{QDIR}/{name}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

ch1, ch2, ch3, ch4, ch5 = load("ch1"), load("ch2"), load("ch3"), load("ch4"), load("ch5")

CHAPTERS = [
    ("lat", "fs-centre-lathe", "Centre Lathe & Lathe Operations", ch1.CH1),
    ("shp", "fs-shapers-planers", "Shapers & Planers", ch2.CH2),
    ("drl", "fs-drilling", "Drilling Machines", ch3.CH3),
    ("mil", "fs-milling", "Milling Process", ch4.CH4),
    ("grd", "fs-grinding", "Grinding Process", ch5.CH5),
]

# Proportional quota for exactly 100 questions (all calculation questions kept)
QUOTA = {"lat": 35, "shp": 18, "drl": 14, "mil": 17, "grd": 16}

# ===========================================================================
# SLIDE-CONTEXT NOTES — (keywords, section title, note)
# Written from the OCR content of "AEE202 slides" (First Shared Slide).
# ===========================================================================
SECTIONS = {
    "lat": [
        (["cutting speed", "cutting fluid", "tungsten carbide", "non-ferrous"],
         "Cutting Speed & Cutting Fluids",
         "The slide states that the optimum cutting speed depends on the tool material, the material to be cut and whether a cutting fluid is used. Recommended cutting speed for cast iron and mild steel with HSS tools is 35 m/min; with tungsten carbide tools 65\u201370 m/min may be used; non-ferrous materials allow much higher speeds. Cutting fluid removes heat from the cutting area and lubricates the tool face so chip\u2013tool friction reduces, making the process more efficient and improving tool life and performance."),
        (["engine lathe", "cylindrical surfaces", "commonest and oldest"],
         "The Centre Lathe",
         "The slide states: \u201cA centre lathe is also called an engine lathe.\u201d It is one of the commonest and oldest machine tools and one of the most versatile and widely used machines; its main function is the production of cylindrical surfaces."),
        (["machine bed", "guide ways"],
         "Machine Bed",
         "The machine bed holds or supports all other parts of the lathe. The top of the bed is formed with machined guide ways on which the carriage slides along the length of the lathe."),
        (["headstock", "hollow spindle", "lubricating oil", "changing gears"],
         "Headstock",
         "The headstock is fixed at the extreme left hand of the bed. It contains shafts and gears immersed in lubricating oil; the driving shaft is driven by an electric motor, and the driven shaft (a hollow spindle) can be driven at various r.p.m. by changing gears. A chuck (either three jaw or four jaw) is screwed on this spindle; when the spindle rotates, the chuck and the work piece rotate about the longitudinal axis of the spindle."),
        (["tailstock", "dead centre", "live centre"],
         "Tailstock",
         "The tailstock is provided at the right hand end of the bed; it slides along the guide ways and can be clamped in the desired position. The axis of its spindle coincides with the axis of the headstock spindle (same height above the bed). The front portion of the tailstock spindle carries a centre (dead centre). If the centre rotates along with the work piece it is called a live centre; if it does not rotate and the work piece alone rotates, it is called a dead centre."),
        (["carriage", "cross slide", "compound rest", "apron", "lead screw", "feed shaft"],
         "Carriage, Cross Slide & Compound Rest",
         "The carriage slides along the bed from the tailstock end to the headstock end; its traversing motion is controlled by the hand traversing wheel or automatically by engaging the feed rod/feed shaft. The cross slide moves crosswise at right angles to the bed. Mounted on it is the compound rest (tool post slide), which rotates in a horizontal plane (normal position 0\u00b0, parallel to bed); its angle is read on a protractor and it is used in taper turning to set the tool for angular cuts; it moves only manually. The apron hides the gears/clutches. Of the two long shafts, the screwed one is the lead screw (used in screw cutting) and the plain one is the feed shaft (used in other operations like turning); they are engaged one at a time."),
        (["size of a lathe", "swing", "radius of the largest"],
         "Size & Swing of a Lathe",
         "The size of a lathe is specified by the distance between the headstock chuck and the tailstock centre \u2014 the length of the longest job that can be machined. The swing is the vertical distance between the chuck centre and the lathe bed, and it gives the radius of the largest work piece which can be turned on the machine."),
        (["3-jaw", "4-jaw", "centering", "self centering"],
         "Holding & Centering the Work Piece",
         "The 3-jaw chuck is a self-centering device used for clamping round stock; the 4-jaw chuck clamps irregularly shaped jobs, and each jaw moves radially independent of the other jaws. Centering means the centre line of the work piece coincides with the centre line of the machine spindle."),
        (["turning operation", "depth of cut", "feed is measured", "cutting speed can be calculated", "tip of the tool", "feed per minute", "feed/rev", "advancing"],
         "Turning Operation",
         "The work piece rotates at a suitable r.p.m. to give the recommended cutting speed; if d is the diameter and N the r.p.m., the cutting speed v = \u03c0dN. The tool tip is set at the same height as the job centre; the tool is inserted by the cross slide at the right hand end with a depth of cut of 1\u20131.5 mm, then traversed right to left by sliding the carriage on the bed. Feed is measured in mm/rev of the work piece, so feed per minute = N \u00d7 feed/revolution. If the reduction cannot be done in one pass, the tool is brought back and advanced again by 1\u20131.5 mm; the process repeats until the desired diameter is reached."),
        (["facing", "datum", "flat circular"],
         "Facing",
         "In facing, the work piece rotates but the tool is moved across by feeding the cross slide while the carriage is locked in one position. The result is a flat circular section at one end of the cylinder; all lengths are then measured taking this surface as datum during further machining."),
        (["taper", "half angle", "set over", "form tool", "attachment"],
         "Taper Turning",
         "Taper turning produces a conical surface by gradual reduction in diameter; the tool must move along a line inclined to the longitudinal axis of the work piece, and the taper is defined by the half angle (\u03b1) of the cone. Methods: (1) swivelling the compound rest through the half cone angle and feeding with the compound rest handwheel \u2014 accurate conical surface; (2) setting over the tailstock centre at right angles to the machine axis (the tailstock base guide ways have clearance allowing limited lateral shift) \u2014 the tool traverses parallel to the machine centre line while the work axis is inclined; suitable for small taper angles because the set over cannot be measured accurately; (3) a taper turning attachment fitted on the backside of the cross slide \u2014 accurate production of a wide range of tapers; (4) a form tool whose front profile cuts the taper when plunged \u2014 only very short tapers, and the tool profile must be short or the work and tool will vibrate."),
        (["parting", "plunge cut", "profile or form turning"],
         "Parting & Profile (Form) Turning",
         "Parting is performed with a parting tool and requires a plunge cut; the carriage remains locked, and when the tool tip reaches the centre line the job parts into two pieces. Profile/form turning generates forms like a specified radius or semicircular shape with a suitably shaped form tool and a plunge cut (only the cross slide is used)."),
        (["boring", "enlarging an existing hole", "drill is inserted", "boring bar"],
         "Boring & Initial Drilling",
         "Boring means enlarging an existing hole. For initial drilling the tailstock centre is removed and a drill is inserted in the tailstock spindle; the drill is advanced by the tailstock handwheel and afterwards withdrawn. The boring bar fitted with the tool bit must be smaller in diameter than the hole. Boring is really an internal turning operation, and not being able to see the actual cutting makes it tricky and delicate."),
        (["threading", "thread cutting", "screw cutting", "helical grooves", "lead screw", "pitch of threads"],
         "Threading (Screw Cutting)",
         "Threading cuts threads or helical grooves on the cylindrical surface of the job. The carriage is connected to the lead screw, and the pitch of the threads to be cut equals (r.p.m. of lead screw \u00f7 r.p.m. of workpiece) \u00d7 pitch of lead screw \u2014 gears give the required ratio. Threads have a standard profile which the tool profile must match. Screw cutting lathes have reversible motors, and the spindle r.p.m. is kept very low for thread cutting."),
        (["knurling", "diamond shaped", "etched"],
         "Knurling",
         "For better grip, work pieces are given a shallow diamond shaped pattern on the circumference. The knurling rollers (hardened, with a similar pattern on their surface) are clamped in the tool post and pressed into the rotating work by the cross slide; as roller and work rotate together the pattern is etched into the surface. Accessories and fittings greatly improve the performance and range of work on a lathe."),
    ],
    "shp": [
        (["flat surface", "single-point", "interrupted"],
         "Shapers & Planers \u2014 Basics",
         "Shapers and planers produce flat surfaces (horizontal, vertical or inclined) using single-point cutting tools essentially the same as lathe tools. The cutting tool is subjected to intermittent cuts: it cuts in the forward direction and is idle in the return direction."),
        (["machine bed", "ram", "tool post", "clapper box", "vice", "inclined surface", "swivelled in a vertical plane"],
         "Shaper \u2014 Principal Parts",
         "The shaper has a hollow cast iron bed that houses the slotted lever quick return mechanism, which drives a horizontal ram reciprocating in guide ways on top of the frame. A tool post is fitted on the front face of the ram; its slide is operated by a hand wheel, the whole tool post can be raised or lowered, and the tool slide can be swivelled in a vertical plane with its inclination read on a scale in degrees (the tool is inclined for inclined surfaces). The table can be raised/lowered and moved horizontally left or right, and a vice holds the work piece. The clapper box, fitted in the tool post, lifts the tool tip during the return stroke so the machined surface is not spoiled."),
        (["quick return", "slotted lever", "crank", "die block", "angle \u03b1", "angle \u03b2", "short link arm"],
         "Slotted Lever Quick Return Mechanism",
         "Because useful work is done only in the forward stroke, the mechanism is designed so the return stroke takes much less time than the forward stroke. The crank AB (adjustable length R) rotates at uniform angular speed; the crank pin A is a die block that slides in the slot of the slotted lever OBC, which is pivoted at O and connected to the ram by a short link arm. When the crank rotates clockwise from AB\u2081 to AB\u2082 the ram moves forward (left to right), and from AB\u2082 to AB\u2081 it returns. The forward stroke time is proportional to angle \u03b1 and the return stroke time to angle \u03b2."),
        (["high speed steel", "tungsten carbide tools are not preferred", "brazed tips"],
         "Shaper Cutting Tools",
         "Shaper cutting tools are generally made of H.S.S., either solid or with brazed tips, made sturdy with generous shank and tip sizes because of intermittent cuts. Due to the intermittent cuts, tungsten carbide tools are not preferred for shaping work."),
        (["stroke of its ram", "60\u201370 mm", "30\u201335 mm", "feed is given", "depth of cut is given", "contour cutting"],
         "Using the Shaper",
         "The size of a shaper is denoted by the maximum length of stroke of its ram. The stroke is kept about 60\u201370 mm longer than the job; by changing where the short link arm connects to the ram, the stroke starts 30\u201335 mm before the job and ends 30\u201335 mm beyond it. The stroke length is altered by changing the crank AB length. Depth of cut is given by rotating the hand wheel and lowering the tool slide (not by raising the table); table height is set only when fixing the job. Feed is given by shifting the table laterally \u2014 manually or automatically \u2014 during the return stroke of the ram. Contour cutting calls for simultaneous horizontal table feed and vertical hand feed of the tool, so only a very skilled operator can do it."),
        (["planer", "too large and heavy", "stationary", "moves past", "more than one tool post", "squareness"],
         "The Planer",
         "A planer machines flat surfaces on work pieces too large and heavy for a shaper table. The fundamental difference: in a planer the cutting tool remains stationary and the table (with the clamped work) moves past the tool; the feed is given to the cutting tool, not the table. The planer can take much heavier cuts and has more than one tool post, so a horizontal and a vertical surface can be machined simultaneously and their squareness is automatically ensured. The cast iron bed has Vee guide ways machined along its length and is grouted in the ground; the table has a long rack in the centre of its width for reciprocating motion and T-slots on top for clamping. A cross rail slides up and down on two vertical columns; usually one or two tool heads are mounted on the cross rail and one side tool head on each column (vertical heads move laterally on the cross rail, side heads move up and down the columns)."),
        (["limit switches", "reversible motor", "average speed", "per cutting stroke", "T-slot cutting"],
         "Planer Drive & Tools",
         "To save idle time, the return stroke of the planer table takes place at higher speed, achieved by a variable speed reversible motor drive and limit switches fitted on the bed which actuate when the table reaches the end of its strokes; the stroke length is adjusted by changing the limit switch positions. Cutting speed is calculated on the basis of the average speed during the forward stroke. Feed is the lateral distance moved by the tool (on the cross rail) per cutting stroke, and feed and depth of cut are both expressed in mm. Planer tools are HSS (occasionally tipped carbide), more robust than shaper tools; specially shaped tools are used for T-slot cutting and dove tail slide cutting."),
    ],
    "drl": [
        (["drilling means", "twist drill", "multiple point"],
         "Drilling & the Twist Drill",
         "Drilling means making a hole in a solid metal piece with a rotating tool called a drill. In the olden days a flat drill was used, but now a twist drill is universally used. A twist drill has two cutting edges, hence it is a multiple point cutting tool."),
        (["taper shank", "collet", "lips", "flutes", "118"],
         "Twist Drill Nomenclature & Fitting",
         "Twist drills usually have a taper shank fitted into the machine spindle's tapered sleeve of matching taper \u2014 when the sleeve rotates, friction between the tapered surfaces rotates the drill. A parallel shank needs a special collet chuck. The drill has two lips at the cutting end; the angle between the two cutting lips is usually 118\u00b0. Chips formed at the cutting edges are guided upwards through the helical grooves called flutes, otherwise chips would interfere with cutting."),
        (["torque", "axial force", "machine feed", "chisel edge", "punch", "high speed steel, hardened"],
         "Drill Forces & Starting the Cut",
         "A torque is applied to rotate the drill and overcome cutting resistance; an axial force (provided by the machine feed, expressed in mm per revolution of the drill) keeps pushing the drill deeper. The drill will not start cutting until the chisel edge penetrates the metal surface by about a mm or so, because the chisel edge does not allow the cutting edges to contact the metal; to facilitate cutting, a little depression is made with a punch at the centre of the hole. Twist drills are solid high speed steel, hardened and ground to shape; drills with carbide inserts are also available."),
        (["sensitive", "pillar", "radial", "multispindle"],
         "Types of Drilling Machines",
         "Four types: (1) Sensitive \u2014 light duty, drills up to 12 mm diameter maximum, high spindle speeds, feed by gently turning the hand wheel which lowers the spindle, and the job is aligned so the hole centre is exactly below the spindle. (2) Pillar type \u2014 similar but for heavier work; with a rectangular column the table can be swung aside and bigger jobs placed on the machine base. (3) Radial \u2014 for bigger and heavier work pieces; the drilling head is mounted on a radial arm which rotates around the round column and the head moves in or out along the arm, so (think of polar coordinates \u03b8, r) any point of the work can be reached without shifting the heavy work piece. (4) Multispindle \u2014 more than one spindle drills holes at one time; very useful for mass production work."),
        (["core drilling", "step drilling", "counter boring", "counter sinking", "reaming", "reamer", "tapping", "tap set", "machine tap"],
         "Allied Operations on Drilling Machines",
         "Core drilling: holes made in castings by cores are rough and are cleaned with a core drill. Step drilling: more than one diameter is ground on the drill body, saving an extra operation. Counter boring: a flat surface round a hole for a good seating of washer/bolt heads/nuts; the tool's pilot keeps the counterbore concentric with the hole. Counter sinking: a tapered entrance to the hole, cut with a special tool with a pilot. Reaming: sizing and improving the geometry and finish of a drilled hole; hand, machine and shell reamers exist \u2014 machine reamers are used with the drilling machine; for holes up to 12.5 mm diameter about 0.38\u20130.4 mm of material is left as reaming allowance, and a reamer follows the original hole and cannot shift its centre. Tapping: cutting internal threads with a special flexible adapter holding machine taps; a machine tap set has two taps \u2014 rough and finish \u2014 used in the same order; the spindle r.p.m. is drastically reduced and a good lubricant is used."),
    ],
    "mil": [
        (["milling is a machining process", "several cutting edges", "multiple point", "surface finish"],
         "Milling \u2014 Introduction",
         "Milling is a machining process performed with a rotary cutter with several cutting edges arranged on its periphery; it is a multiple point cutting tool used with a milling machine. It generates flat surfaces, curved profiles and many intricate shapes with great accuracy and very good surface finish; milling machines are essential in any modern machine shop."),
        (["up milling", "down milling", "backlash eliminator", "thickness of chip"],
         "Up Milling vs Down Milling",
         "In up milling (conventional), the cutter rotation and work feed are opposite to each other; the chip thickness at the start is nil and is maximum when the teeth leave the work surface, and the teeth try to uproot and lift the work piece from the table. In down milling (climb), cutter and feed move in the same direction at the point of contact and it is the reverse; technically down milling is superior but it is not used unless the machine is fitted with a backlash eliminator."),
        (["\u03c0DN", "one pass", "feed per rev", "per tooth", "L + D", "intermittent", "impact loads", "vibration", "metal removal rate"],
         "Milling Speeds, Feeds & Traverse",
         "If the cutter diameter is D and it rotates at N r.p.m., the cutting speed at the tooth tips is \u03c0DN metres/minute, which should conform to recommended values. The cutter is usually wider than the work piece, so one pass is all that is required. Feed of the work piece is measured in mm/minute, but the correct measure is mm of work piece per revolution of cutter per tooth \u2014 if the table feed is f mm/minute and the cutter has Z teeth, feed per rev per tooth = f/(NZ). Metal removal rate in milling is much higher than in shaping or planing. The minimum table traverse is L + D, where L is the job length and D the cutter diameter (D/2 is the minimum overlap on either side so the cutter becomes clear of the job). Unlike turning, milling involves intermittent cutting and a non-uniform chip cross-section; high impact loads at entry and fluctuating cutting forces cause vibration and chatter, which strongly influences cutter design."),
        (["peripheral milling", "face milling", "arbor", "overhang", "symmetrical", "asymmetric"],
         "Peripheral vs Face Milling",
         "In peripheral milling the cutting edges are on the circumference and the milled surface is generally parallel to the cutter axis; the cutters are supported on a long arbor whose deflection restricts dimensional and form accuracy, and these operations are usually done on a horizontal milling machine. In face milling the generated surface is parallel to the cutter face and perpendicular to the cutter axis; the cutter overhang is limited, giving better dimensional control and flatness, and face cutters are used with a vertical milling machine. Face milling is a combination of up cut and down cut. The cutter may be placed symmetrically on the work, or asymmetrically offset slightly towards the entry or exit side; asymmetric milling with larger chip thickness at entry and smaller at exit is ideal and should be adopted."),
        (["slab milling", "slot milling", "side and face", "form milling", "straddle", "gang", "arbor of a horizontal", "tungsten carbide", "throw away"],
         "Milling Operations",
         "Peripheral milling operations: (1) slab milling \u2014 flat surfaces; (2) slot milling \u2014 precision slots; (3) side and face milling \u2014 adjacent horizontal and vertical surfaces simultaneously; (4) form milling \u2014 prismatic shapes of any form, e.g. the involute form in gear cutting; (5) straddle milling \u2014 two parallel vertical faces; (6) gang milling \u2014 a number of surfaces simultaneously with a set of cutters. The hole and keyway in the centre of peripheral cutters mount them on the arbor of a horizontal milling machine. Cutters are solid HSS or have tungsten carbide blades, brazed or with throw away inserts."),
        (["end mills", "die sinking", "sculpted", "taper shank"],
         "End Mills",
         "End mills perform a combination of peripheral and face milling simultaneously, having cutting edges on the bottom face and the periphery. They are used for edges, shoulders, grooves, slots and keyway pockets, and widely for die sinking and generation of sculpted surfaces. They come in cobalt HSS (super HSS), coated HSS, solid carbide, and indexable inserts of cemented/coated carbide. End mills have a taper shank fitting the taper sleeve in the spindle of a vertical milling machine."),
        (["milling machines come in three", "knee", "dividing head", "helix", "arbor supporting bracket", "hollow spindle", "traversed at high speed", "vertical milling machine", "does not have an arbor", "plain version", "production work", "horizontal milling machine"],
         "Milling Machines",
         "Milling machines come in three basic models: horizontal, vertical and universal (a horizontal type with special features). The most common is the horizontal knee type \u2014 the knee slides up and down the front of the machine and carries the saddle and table. The universal machine's table is mounted on a turn table and can swivel in a horizontal plane, permitting the cutting of helix, and includes a dividing head for indexing; the plain version is more robust and better for production work. On the horizontal machine, the arbor fits into the spindle nose and extends a little beyond the arbor supporting bracket; when end mills/face cutters/drills are used, the arbor is removed and the taper shank fits into the hollow spindle, so vertical faces can be milled without difficulty. The table can be given hand feed or auto feed and can also be traversed at high speed. The vertical milling machine has no arbor \u2014 it has a vertical spindle for end mills, face milling cutters and drills."),
    ],
    "grd": [
        (["emery", "corundum", "bond", "second in hardness only to diamond", "tiny cutting tool", "chip producing", "hardened steel", "hardened high speed steel"],
         "Grinding \u2014 Introduction",
         "In grinding, an emery or corundum wheel is the cutting tool; emery and corundum are naturally found abrasives, impure forms of aluminium oxide (Al\u2082O\u2083). The wheel consists of thousands of tiny abrasive particles embedded in a matrix called the bond. An abrasive is extremely hard \u2014 second in hardness only to diamond. As the wheel rotates, each particle acts like a tiny cutting tool machining material away; under a magnifying lens the metal dust shows all the characteristics of metal chips, so grinding is truly a chip producing machining process. It produces very accurate sizes, equally accurate geometry and roundness, and extremely good surface finish, and it can machine hardened steel and even hardened HSS which other processes cannot."),
        (["glazing", "break away", "prematurely"],
         "Wheel Sharpening Behaviour",
         "When the sharp edges of the abrasive grains become dull, they should split to form new edges or break away to expose the next layer of grains. If dulled grains stay in the wheel and keep rubbing without actually cutting, the defect is called glazing; if grains break away or split prematurely before becoming dull, it causes reduction in the life of the grinding wheel."),
        (["silicon carbide", "aluminium oxide", "greenish black", "code for silicon carbide"],
         "Choice of Abrasives",
         "Emery and corundum are no longer used; artificial (manufactured) abrasives are used for their high purity: (a) silicon carbide \u2014 greenish black, harder and more brittle than alumina, used for materials of low grinding resistance like cast iron, brass and copper; (b) aluminium oxide (Al\u2082O\u2083) \u2014 brownish, used for grinding steel because of its greater toughness. The code for silicon carbide is C and for Al\u2082O\u2083 wheels it is A."),
        (["grit", "flours", "jewellers", "bond", "grade", "vitrified", "silicate", "shellac", "rubber", "resinoid", "structure", "10% to 30%"],
         "Wheel Classification \u2014 Grit, Grade, Bond & Structure",
         "Grit indicates the abrasive grain size; the higher the number, the finer the grains. Abrasives finer than 200 are called 'flours' (F, FF, FFF) and are used by jewellers. Finer wheels give a fine finish but limited metal cutting capacity; coarser wheels give a rough finish but higher metal removal. The bond is the matrix substance, and the degree of hardness of the bond is the grade \u2014 the strength with which the grains are held. Bonds: vitrified (V, about 80% of wheels in industry), silicate (S, silicate of soda), shellac (E), rubber (R, abrasive kneaded in rubber and moulded), resinoid (B, bakelite). Grade is indicated by alphabet letters: A = very soft, Z = very hard, M and N = medium. Structure depends on the percentage of bond material (about 10% to 30% of wheel volume): tightly packed grains with less bond = closed structure; loosely packed = open structure; structure is indicated by a number from 1 (very closed) to 15 (very open). Manufacturers must mark on every wheel, in sequence: abrasive used (A or C), grit number, grade, structure and bond type."),
        (["wheel selection", "hard wheel for soft material", "balancing", "many thousand r.p.m.", "truing", "diamond tool", "square"],
         "Wheel Selection, Mounting & Truing",
         "Wheel selection depends on the abrasive and wheel characteristics and on operating conditions like wheel and work speed, relative diameters, and machine type/condition \u2014 it is best to follow the wheel manufacturer's recommendations. Thumb rule: use a hard wheel for soft material and a soft wheel for hard material (a hard wheel retains its abrasives because they do not dull easily on soft material). A grinding wheel is delicate and fragile \u2014 correct mounting and balancing are of utmost importance because wheels revolve at many thousand r.p.m. and unbalanced centrifugal forces may crack the wheel or spoil the bearings. A freshly fitted wheel must be trued (face and sides) so it becomes square to the work piece; truing/dressing is also needed later to correct non-uniform wear or to open up the face for efficient cutting. Truing/dressing is done by a diamond tool, which is harder and can cut through the abrasive grains and the bond material."),
        (["cylindrical grinding", "0.015", "between two centres", "universal", "internal grinding"],
         "Cylindrical Grinding",
         "The cylindrical grinding machine comes in two varieties \u2014 plain and universal \u2014 with the same fundamental design, but the universal machine can also be adopted for internal grinding. The work is mounted between two centres and rotated, while the grinding wheel, mounted on a spindle, revolves at much higher r.p.m. The work and centres sit on a table that traverses at various feeds so the entire length of the work passes to and fro in front of the wheel. The depth of cut is very small, about 0.015 mm; when the entire length has passed, the wheel advances another 0.015 mm at the end of the traverse, and the cycle continues until the desired diameter is reached. The result is a long cylinder of perfectly circular profile with very fine surface finish."),
    ],
}

# Generic fallback note per chapter
FALLBACK = {
    "lat": "This question comes from the Centre Lathe section of the First Shared Slide (Manufacturing Processes). The centre lathe (engine lathe) produces cylindrical surfaces; its main parts are the bed, headstock, tailstock and carriage, and its operations include turning, facing, taper turning, profile turning, parting, boring, threading and knurling.",
    "shp": "This question comes from the Shapers & Planers section of the First Shared Slide. Shapers and planers produce flat surfaces with single-point tools under intermittent cuts; the shaper uses a slotted lever quick return mechanism, and the planer moves the table past a stationary tool.",
    "drl": "This question comes from the Drilling Machines section of the First Shared Slide. Drilling makes a hole with a rotating twist drill (a multiple point cutting tool); the four machine types are sensitive, pillar, radial and multispindle, and allied operations include core drilling, step drilling, counter boring, counter sinking, reaming and tapping.",
    "mil": "This question comes from the Milling Process section of the First Shared Slide. Milling uses a rotary multiple point cutter; the two basic processes are up (conventional) and down (climb) milling, and the process is classified into peripheral and face milling, with operations such as slab, slot, side & face, form, straddle and gang milling.",
    "grd": "This question comes from the Grinding Process section of the First Shared Slide. Grinding uses an emery/corundum wheel of bonded abrasive grains, each acting as a tiny cutting tool; modern wheels use silicon carbide (C) or aluminium oxide (A) abrasives, classified by grit, grade, structure and bond.",
}


def find_section(chapter, q):
    """Pick the best-matching section note for a question."""
    text = (q["q"] + " " + q["exp"]).lower()
    best, best_score = None, 0
    for keywords, title, note in SECTIONS[chapter]:
        score = sum(1 for k in keywords if k.lower() in text)
        if score > best_score:
            best, best_score = (title, note), score
    if best is None:
        return "First Shared Slide \u2014 Context", FALLBACK[chapter]
    return best


def first_sentence(exp):
    s = exp.strip()
    # trim common lead-ins for the `short` field
    for lead in ("The slide states: ", "The slide states ", "The slide states that "):
        if s.startswith(lead):
            s = s[len(lead):]
    s = re.sub(r"^\u201c|\u201d$", "", s)
    cut = s
    for i, ch in enumerate(s):
        if ch in ".!?" and i > 30:
            cut = s[: i + 1]
            break
    return cut[:170].strip()


def is_calc(q):
    return q["q"].startswith("CALCULATION")


def clean_qtext(t):
    t = t.replace("CALCULATION. ", "").strip()
    return t


def spread(items, need):
    """Deterministic even-spread sample of `need` items."""
    if need <= 0 or not items:
        return []
    if need >= len(items):
        return list(items)
    picks = []
    step = len(items) / need
    for i in range(need):
        idx = int(i * step + step / 2)
        if idx >= len(items):
            idx = len(items) - 1
        picks.append(items[idx])
    # de-dupe preserving order, fill from the rest if short
    seen, out = set(), []
    for p in picks:
        if id(p) not in seen:
            seen.add(id(p))
            out.append(p)
    for p in items:
        if len(out) >= need:
            break
        if id(p) not in seen:
            seen.add(id(p))
            out.append(p)
    return out


def build():
    out = []
    counts = {}
    for key, topic_id, topic_name, bank in CHAPTERS:
        questions = [q for q in bank if not q.get("fig")]
        calc = [q for q in questions if is_calc(q)]
        normal = [q for q in questions if not is_calc(q)]
        quota = QUOTA[key]
        picked = list(calc[:quota])
        need = quota - len(picked)
        picked += spread(normal, need)
        # trim to quota exactly
        picked = picked[:quota]
        counts[key] = 0
        for q in picked:
            counts[key] += 1
            ans_idx = ord(q["ans"]) - 65
            exp = q["exp"]
            sec_title, sec_note = find_section(key, q)
            solution = (
                exp
                + "\n\n\U0001F4D8 From the First Shared Slide \u2014 "
                + sec_title
                + ":\n"
                + sec_note
            )
            out.append({
                "id": f"aee_fs_{key}_{counts[key]:02d}",
                "topicId": topic_id,
                "question": clean_qtext(q["q"]),
                "options": [o for o in q["opts"]],
                "correct": ans_idx,
                "short": first_sentence(exp),
                "solution": solution,
            })
    return out


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "counts":
        for key, tid, tname, bank in CHAPTERS:
            qs = [q for q in bank if not q.get("fig")]
            print(key, "total", len(qs), "calc", sum(1 for q in qs if is_calc(q)))
    else:
        qs = build()
        json.dump(qs, open(".first_slides_out.json", "w"), ensure_ascii=False, indent=2)
        by_topic = {}
        for q in qs:
            by_topic[q["topicId"]] = by_topic.get(q["topicId"], 0) + 1
        print("TOTAL:", len(qs))
        for k, v in by_topic.items():
            print(" ", k, "->", v)
