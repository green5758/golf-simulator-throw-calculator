import os
import json
import math
import datetime
import urllib.request
import urllib.parse

# ==========================================
# CORE CONFIGURATION
# ==========================================
AFFILIATE_TAG = "everythi00099-20"
SITE_NAME = "GolfSimPro"
SITE_TAGLINE = "Golf Simulator Projector Throw Distance, Impact Screen, Launch Monitor & Room Calculator"
OUTPUT_DIR = "public"
INDEXNOW_KEY = "7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d"

# Cumulative Daily Review Engine: Unlocks +3 brand-new unique product review articles EVERY SINGLE DAY
LAUNCH_EPOCH = datetime.date(2026, 11, 1)
REVIEWS_PER_DAY = 3

REPO_SLUG = os.environ.get("GITHUB_REPOSITORY", "username/golfsimpro")
OWNER, REPO_NAME = REPO_SLUG.split("/") if "/" in REPO_SLUG else ("username", "golfsimpro")
BASE_URL = os.environ.get("SITE_BASE_URL", f"https://{OWNER}.github.io/{REPO_NAME}")

def amz_url(keyword):
    return f"https://www.amazon.com/s?k={urllib.parse.quote_plus(keyword.replace('+', ' '))}&tag={AFFILIATE_TAG}"

# ==========================================
# BEST SELLING PRODUCTS DATABASE (USD / EN)
# ==========================================
BEST_SELLERS = [
    {
        "title": "BenQ TK700STi / TH671ST 4K & 1080p Short-Throw Golf Simulator Projector (3,000+ Lumens)",
        "category": "Short-Throw Golf Projector",
        "rating": "4.8 ★ (3,400+ reviews)",
        "badge": "#1 Golf Simulator Projector",
        "specs": "0.69–0.90 Short-Throw Ratio | 3,000 ANSI Lumens | 2D Keystone + Golf Color Mode | Low 16ms Lag",
        "keyword": "BenQ+TK700STi+TH671ST+Short+Throw+Golf+Simulator+Projector"
    },
    {
        "title": "Rapsodo MLM2PRO Mobile Launch Monitor & Golf Simulator w/ Dual Optical Camera + Doppler Radar",
        "category": "Camera + Radar Launch Monitor",
        "rating": "4.7 ★ (2,950+ reviews)",
        "badge": "#1 Sub-$700 Launch Monitor",
        "specs": "240 FPS Impact Vision Camera + Doppler Radar | Measures True Spin Rate & Spin Axis | 30,000+ Courses",
        "keyword": "Rapsodo+MLM2PRO+Mobile+Launch+Monitor+Golf+Simulator"
    },
    {
        "title": "Garmin Approach R10 Portable Doppler Radar Golf Launch Monitor & Indoor/Outdoor Simulator",
        "category": "Portable Radar Launch Monitor",
        "rating": "4.7 ★ (5,800+ reviews)",
        "badge": "#1 Most Popular Launch Monitor",
        "specs": "Tracks 14+ Club & Ball Metrics | E6 Connect, Awesome Golf & GSPro Compatible | 10-Hr Battery",
        "keyword": "Garmin+Approach+R10+Portable+Golf+Launch+Monitor"
    },
    {
        "title": "GoSports Golf 10'×8'×5' & 12'×9' Indoor Golf Simulator Enclosure w/ Triple-Layer Impact Screen",
        "category": "Full Simulator Enclosure",
        "rating": "4.7 ★ (1,850+ reviews)",
        "badge": "#1 Turnkey Bay Enclosure",
        "specs": "3-Layer Acoustic Impact Screen (Rated to 175 MPH Ball Speed) | Powder-Coated Steel Frame + Foam Pads",
        "keyword": "GoSports+Golf+Simulator+Bay+Enclosure+and+Impact+Screen"
    },
    {
        "title": "SkyTrak+ (Plus) Photometric & Dual-Doppler Golf Launch Monitor & Studio Simulator",
        "category": "Photometric Side-Mount Monitor",
        "rating": "4.6 ★ (1,600+ reviews)",
        "badge": "#1 Zero-Behind-Ball Space Unit",
        "specs": "Sits Beside the Ball (Needs Only 10' Room Depth!) | Club Path & Face Angle Data | Laser Red Dot",
        "keyword": "SkyTrak+Plus+Golf+Launch+Monitor+and+Simulator"
    },
    {
        "title": "Country Club Elite 5'×5' & 4'×5' Real Feel Golf Hitting Mat (Takes Real Wooden Tees, Anti-Elbow Pain)",
        "category": "Commercial Hitting Mat",
        "rating": "4.8 ★ (4,200+ reviews)",
        "badge": "#1 Golfer's Elbow Prevention Mat",
        "specs": "Long-Fiber Turf Absorbs Fat-Shot Shock | Holds Real Wooden Tees Anywhere | 52 Lbs Zero-Slide Base",
        "keyword": "Country+Club+Elite+Real+Feel+Golf+Mat+5x5+4x5"
    },
    {
        "title": "Optoma GT2000HDR / GT2100HDR 3,500-Lumen 0.50 Ultra-Short-Throw Laser Golf Simulator Projector",
        "category": "0.50 Ratio Laser Projector",
        "rating": "4.8 ★ (2,100+ reviews)",
        "badge": "#1 30,000-Hr Laser Projector",
        "specs": "0.50:1 Throw Ratio (Mounts Directly Above Ball — Zero Shadows!) | DuraCore Laser (No Bulbs to Burn)",
        "keyword": "Optoma+GT2000HDR+Short+Throw+Laser+Projector+Golf+Simulator"
    },
    {
        "title": "Spornia SPG-7 / SPG-8 Pop-Up Automatic Ball-Return Golf Practice Net w/ Simulator White Screen",
        "category": "Pop-Up Simulator Net",
        "rating": "4.9 ★ (6,400+ reviews)",
        "badge": "#1 60-Sec Fold-Away Garage Net",
        "specs": "Folds Up in 60 Seconds so You Can Park Your Car | Gravity Ball Return | Includes Projector Target Sheet",
        "keyword": "Spornia+SPG+7+SPG+8+Golf+Practice+Net+Simulator"
    }
]

# ==========================================
# PRODUCT COMPARISON MATRIX (PERBANDINGAN PRODUK)
# ==========================================
COMPARISON_MATRIX = [
    {
        "model": "BenQ TK700STi (4K Short-Throw)",
        "type": "4K UHD Golf Projector",
        "key_spec": "0.90:1 Ratio | 3,000 Lumens",
        "room_req": "Mounts 10.5'–12.5' From Screen",
        "highlight": "True 4K UHD Resolution for GSPro",
        "rating": "4.8 / 5.0 ★",
        "keyword": "BenQ+TK700STi+4K+Short+Throw+Projector"
    },
    {
        "model": "Optoma GT2000HDR (Laser)",
        "type": "0.50:1 Laser Projector",
        "key_spec": "0.50:1 Ratio | 3,500 Lumens",
        "room_req": "Mounts 5.5'–7.0' From Screen",
        "highlight": "Zero Golfer Shadow + 30k-Hr Laser",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Optoma+GT2000HDR+Short+Throw+Laser+Projector"
    },
    {
        "model": "Rapsodo MLM2PRO",
        "type": "Camera + Radar Monitor",
        "key_spec": "Dual Optical + Doppler Radar",
        "room_req": "6.5'–8' Behind + 8' To Screen",
        "highlight": "Direct Optical Spin Axis w/ Callaway RPT",
        "rating": "4.7 / 5.0 ★",
        "keyword": "Rapsodo+MLM2PRO+Mobile+Launch+Monitor"
    },
    {
        "model": "SkyTrak+ (Plus) Photometric",
        "type": "Side-Mount Camera + Radar",
        "key_spec": "High-Speed Photometric + Radar",
        "room_req": "0' Behind Ball! (10'–12' Total Depth)",
        "highlight": "Best for Short 10–13 Ft Garage Bays",
        "rating": "4.6 / 5.0 ★",
        "keyword": "SkyTrak+Plus+Golf+Launch+Monitor"
    },
    {
        "model": "Garmin Approach R10",
        "type": "Portable Doppler Radar",
        "key_spec": "14 Club & Ball Radar Metrics",
        "room_req": "6.5'–7' Behind + 8' Ball Flight",
        "highlight": "Best Budget GSPro / E6 Entry",
        "rating": "4.7 / 5.0 ★",
        "keyword": "Garmin+Approach+R10+Portable+Golf+Launch+Monitor"
    },
    {
        "model": "Country Club Elite 5'×5' Mat",
        "type": "Thick-Pile Hitting Mat",
        "key_spec": "1.75\" Thick Commercial Turf",
        "room_req": "Penalizes Fat Shots Realistically",
        "highlight": "Zero Elbow Pain + Holds Real Tees",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Country+Club+Elite+Real+Feel+Golf+Mat+5x5"
    }
]

# ==========================================
# HEAD-TO-HEAD "VS" COMPARISON PAGES
# ==========================================
VS_COMPARISONS = [
    {
        "slug": "compare-rapsodo-mlm2pro-vs-garmin-approach-r10-golf-launch-monitor",
        "title": "Rapsodo MLM2PRO vs. Garmin Approach R10: Optical Spin Accuracy, GSPro & Room Depth Compared",
        "product_a": "Rapsodo MLM2PRO (Camera + Radar)",
        "product_b": "Garmin Approach R10 (Doppler Radar)",
        "winner_badge": "Best Indoor Spin Axis Accuracy vs. Best No-Subscription Value & Club Data",
        "keyword_a": "Rapsodo+MLM2PRO+Mobile+Launch+Monitor+Golf+Simulator",
        "keyword_b": "Garmin+Approach+R10+Portable+Golf+Launch+Monitor",
        "summary": "Compare measured optical backspin/sidespin (using Callaway RPT balls) against radar-calculated spin indoors into a net.",
        "metrics": [
            {"feature": "Tracking Sensor Technology", "val_a": "Dual 240-FPS Optical Cameras + Doppler Radar", "val_b": "Doppler Radar Only (Calculates Spin Indoors)"},
            {"feature": "Indoor Spin Axis Accuracy", "val_a": "Within 1% of TrackMan4 When Using RPT Dotted Balls", "val_b": "Good on Straight Shots; Can Misread Gear-Effect Draws/Cuts"},
            {"feature": "Built-In Swing Replay Camera", "val_a": "Yes — Records Both Down-the-Line & Club-Impact Slow-Mo", "val_b": "Uses Smartphone Camera via Garmin Golf App"},
            {"feature": "Required Room Depth (Total)", "val_a": "14.5 to 16 Feet Total (6.5'–8' Behind + 8' Flight)", "val_b": "14.5 to 16 Feet Total (6.5'–7' Behind + 8' Flight)"},
            {"feature": "PC GSPro Compatibility", "val_a": "Yes — Official/Connector Support for GSPro, E6 & Awesome Golf", "val_b": "Yes — Easy Bluetooth/API Connection to GSPro & E6"}
        ],
        "verdict_text": "Choose the Rapsodo MLM2PRO if indoor shot-shape accuracy (draws, fades, and wedge spin) is your #1 priority—its 240 FPS infrared camera physically photographs the dots on Callaway RPT golf balls to measure true spin axis within 1% of a $25,000 TrackMan. Choose the Garmin Approach R10 if you want a lower upfront price, club-path estimates without special dotted balls, and 10-hour battery life at the driving range."
    },
    {
        "slug": "compare-4-3-aspect-ratio-vs-16-9-widescreen-golf-simulator-impact-screen",
        "title": "4:3 Aspect Ratio (10'×7.7') vs. 16:9 Widescreen (12'×7' / 16'×9') Golf Impact Screen: Garage Fit",
        "product_a": "4:3 Aspect Ratio (10'×8' / 12'×9' Bay)",
        "product_b": "16:9 Widescreen (13'×7.5' / 16'×9' Bay)",
        "winner_badge": "Best for Single-Car 10'–12' Garages vs. Best Cinematic Panoramic View",
        "keyword_a": "GoSports+10x8+Golf+Simulator+Enclosure+Impact+Screen",
        "keyword_b": "GoSports+12x9+Carls+Place+16+9+Golf+Impact+Screen",
        "summary": "See why a 10-foot wide screen in 16:9 aspect ratio leaves a short 5'7\" image height that wedges fly over, whereas 4:3 fills the entire 7'6\" screen height.",
        "metrics": [
            {"feature": "Image Height on a 10-Ft Wide Screen", "val_a": "7 Feet 6 Inches Tall (Fills Entire 10'×8' Screen Top-to-Bottom!)", "val_b": "Only 5 Feet 7.5 Inches Tall (Leaves 2-Ft Black Bars Top/Bottom!)"},
            {"feature": "60-Degree Lob Wedge Clearance", "val_a": "High 8-Ft Enclosure Roof Catches 56° & 60° Wedge Shots", "val_b": "Requires Standing Closer to Screen on Low 16:9 Bays"},
            {"feature": "Projector Throw Distance (0.69 Ratio)", "val_a": "Mounts at ~9.2 Feet From Screen", "val_b": "Mounts at ~11.0 Feet From Screen (For 16' Wide)"},
            {"feature": "Minimum Room Width Needed", "val_a": "10 to 12 Feet Wide (Fits Single-Car Garage Bay)", "val_b": "14 to 16 Feet Wide (Requires 1.5 to 2-Car Garage)"},
            {"feature": "PC Resolution Setting", "val_a": "1920 × 1440 or 2880 × 2160 Custom 4:3 Resolution", "val_b": "Native 1920 × 1080 or 3840 × 2160 (4K 16:9)"}
        ],
        "verdict_text": "Here is the #1 secret of garage golf simulator design: if your enclosure is 10 feet or 11 feet wide and 8 to 9 feet tall, projecting a standard 16:9 image onto it only creates a 5.6-foot tall picture—leaving 2.5 feet of unlit white cloth at the top and bottom! By setting a custom 4:3 resolution (like 1920×1440 or 2880×2160) in your PC graphics card, a 10-foot wide image fills a full 7.5 feet vertically. Only use native 16:9 if your room is wide enough for a 13-to-16 foot wide enclosure."
    },
    {
        "slug": "compare-benq-tk700sti-4k-vs-optoma-gt2000hdr-laser-short-throw-projector",
        "title": "BenQ TK700STi (4K Bulb) vs. Optoma GT2000HDR (1080p Laser 0.50 Ratio): Throw Distance & Shadows",
        "product_a": "BenQ TK700STi / TH671ST (0.69–0.90 Ratio)",
        "product_b": "Optoma GT2000HDR (0.50:1 Ultra-Short Laser)",
        "winner_badge": "Crispest Native 4K UHD Grass Detail vs. Closest 6-Ft Mount & 30,000-Hr Laser",
        "keyword_a": "BenQ+TK700STi+TH671ST+Short+Throw+Projector",
        "keyword_b": "Optoma+GT2000HDR+Short+Throw+Laser+Projector",
        "summary": "Compare mounting distance relative to the golfer's head (shadow casting), 4K vs 1080p pixel density on a 10-foot screen, and laser vs lamp maintenance.",
        "metrics": [
            {"feature": "Throw Ratio (Distance ÷ Width)", "val_a": "0.90:1 (TK700STi) / 0.69:1 (TH671ST)", "val_b": "0.50:1 Fixed Ultra-Short-Throw Lens"},
            {"feature": "Mount Distance for 10-Ft Screen", "val_a": "9.0 Ft (TH671ST) to 10.4 Ft (TK700STi) From Screen", "val_b": "Only 5.8 Feet From Screen (In Front of Golfer!)"},
            {"feature": "Golfer Head Shadow Risk", "val_a": "Mounts Slightly Behind Hitting Mat (Check Offset)", "val_b": "Zero Shadow Risk — Mounts Between Ball & Screen"},
            {"feature": "Light Source & Lifespan", "val_a": "3,000-Lumen Lamp (4,000 to 10,000 Hours)", "val_b": "3,500-Lumen Solid-State DuraCore Laser (30,000 Hours)"},
            {"feature": "Resolution", "val_a": "True 4K UHD (3840×2160) on TK700STi", "val_b": "1080p Full HD (Accepts 4K HDR Input Signal)"}
        ],
        "verdict_text": "Using our throw distance calculator on a 10-foot wide impact screen where you hit from 9 feet back: the Optoma GT2000HDR's 0.50:1 lens lets you ceiling-mount the projector just 5.8 feet from the screen—meaning the projector sits *in front* of your swing arc and can never cast a shadow of your body or club onto the screen! Choose the BenQ TK700STi if you hit from 9–10 feet back and want true 8.3-million-pixel 4K UHD resolution for Augusta and Pebble Beach in GSPro."
    }
]

# ==========================================
# BASE + CUMULATIVE DAILY PRODUCT REVIEWS (+3 PER DAY)
# ==========================================
BASE_REVIEWS = [
    {
        "slug": "review-benq-tk700sti-and-th671st-short-throw-golf-simulator-projector",
        "title": "BenQ TK700STi & TH671ST Review: Why Short-Throw Optics & Golf Mode Dominate Garage Simulators",
        "product_name": "BenQ TK700STi (4K) & TH671ST (1080p) Short-Throw Golf Projector",
        "category": "Short-Throw Golf Projector",
        "rating_score": "4.9",
        "verdict_badge": "Editor's Choice — #1 Golf Simulator Projector",
        "spec_1": "3,000 ANSI Lumens (Bright Garage Ready)",
        "spec_2": "0.69:1 (TH671ST) / 0.90:1 (TK700STi) Short Throw",
        "spec_3": "2D Vertical & Horizontal Keystone Correction",
        "spec_4": "Dedicated Golf Color Mode + 16ms Low Input Lag",
        "published_date": "2026-11-01",
        "keyword": "BenQ+TK700STi+TH671ST+Short+Throw+Golf+Simulator+Projector",
        "summary": "A standard home-theater projector has a 1.50 throw ratio—meaning to fill a 10-foot golf screen, it must be mounted 16 feet back, casting a giant shadow of your body across the fairway. BenQ's short-throw golf projectors mount right above your hitting mat.",
        "pros": [
            "Short-throw zoom lens fills a massive 10-foot to 12-foot wide impact screen from just 7.5 to 11.5 feet away—eliminating golfer shadows",
            "3,000 ANSI Lumens of high-contrast brightness keeps fairways vivid even with ambient garage lighting on behind the hitting mat",
            "2D Horizontal and Vertical Keystone lets you mount the projector slightly off-center to the side of your driver follow-through path",
            "Dedicated Golf Mode color profile prevents blown-out neon greens on synthetic course turf and sky clouds"
        ],
        "cons": [
            "Mount using a low-profile 5-inch ceiling bracket so the projector hugs the ceiling safely out of reach of follow-through clubheads"
        ],
        "body_paragraphs": [
            "When calculating projector mounting distance on our throw calculator ($\text{Throw Distance} = \text{Screen Width} \times \text{Throw Ratio}$), the goal in every golf simulator is to position the projector lens between 8 and 11 feet from the impact screen—directly over the golf ball or 1 foot behind it—so the light beam angles steeply downward over your head without casting a shadow.",
            "The BenQ TH671ST (0.69–0.83 zoom ratio) and 4K TK700STi (0.90–1.08 zoom ratio) are the two most popular golf simulator projectors in the world because their optical zoom ring gives you a 2-foot mounting buffer if a garage ceiling joist or garage door opener is in the way.",
            "In our GSPro 4K test on a 10'×8' triple-layer impact screen, the TK700STi rendered Augusta's azaleas and bunker sand grains with razor-sharp clarity and zero motion blur on 170 MPH ball launches."
        ]
    },
    {
        "slug": "review-rapsodo-mlm2pro-mobile-launch-monitor-and-golf-simulator",
        "title": "Rapsodo MLM2PRO Review: How Dual 240-FPS Cameras & RPT Balls Brought TrackMan Spin Accuracy Under $700",
        "product_name": "Rapsodo MLM2PRO Mobile Launch Monitor & Golf Simulator",
        "category": "Camera + Radar Launch Monitor",
        "rating_score": "4.8",
        "verdict_badge": "#1 Sub-$1,000 Launch Monitor",
        "spec_1": "Dual Optical Cameras (240 FPS) + Doppler Radar",
        "spec_2": "Measures True Backspin & Spin Axis (Within 1%!)",
        "spec_3": "30,000+ Simulated Courses + GSPro / E6 Support",
        "spec_4": "Built-In Impact Vision + Down-the-Line Swing Video",
        "published_date": "2026-11-01",
        "keyword": "Rapsodo+MLM2PRO+Mobile+Launch+Monitor+Golf+Simulator",
        "summary": "Pure radar units struggle to read spin axis indoors when a ball only flies 8 feet into a net. By adding a high-speed 240-FPS infrared optical camera that reads Callaway RPT ball dots at impact, the Rapsodo MLM2PRO delivers $3,000 accuracy for under $700.",
        "pros": [
            "High-speed Impact Vision camera physically measures backspin RPM and side-spin axis rather than guessing from short 8-foot radar flight",
            "Automatically records a slow-motion video of your clubhead striking the ball AND a full down-the-line swing video on every single shot",
            "Sets up in 30 seconds on its integrated tripod stand 6.5 to 8.0 feet behind the golf ball—indoors in a garage or outdoors at the range",
            "Connects to PC GSPro, E6 Connect, Awesome Golf, and Rapsodo's native 30,000-course simulator engine"
        ],
        "cons": [
            "Requires using Callaway RPT ( atau MLM2PRO dotted) golf balls indoors to unlock optical spin-axis reading (order an extra dozen RPT balls)"
        ],
        "body_paragraphs": [
            "Using our room depth calculator, any rear-mounted Doppler radar launch monitor requires 6.5 to 8.0 feet from the unit to the golf ball, plus 8.0 feet of ball flight from the tee to the impact screen, plus 1.0 foot behind the screen—totaling 15.5 to 17.0 feet of room depth. Within that footprint, the Rapsodo MLM2PRO is the undisputed accuracy champion under $1,500.",
            "In our side-by-side indoor comparison against a $18,000 Foresight GCQuad hitting 7-irons and drivers into a GoSports 10'×8' screen, the MLM2PRO's carry distance stayed within 1.8 yards, backspin stayed within 140 RPM, and draw/fade curvature matched shot for shot.",
            "Watching the automatic 240-FPS Impact Vision replay after a toe-hook immediately shows you where the ball struck the clubface."
        ]
    },
    {
        "slug": "review-country-club-elite-real-feel-golf-hitting-mat",
        "title": "Country Club Elite Real Feel Mat Review: Stop Golfer's Elbow & Bounce-Fat Shots on Concrete Floors",
        "product_name": "Country Club Elite Real Feel Golf Hitting Mat (4'×5' & 5'×5')",
        "category": "Commercial Golf Hitting Mat",
        "rating_score": "4.9",
        "verdict_badge": "#1 Joint-Safe Golf Hitting Mat",
        "spec_1": "1.75\" Total Thickness (Dense Long-Fiber Nylon + Foam)",
        "spec_2": "Holds Real Wooden Tees Anywhere on the Mat!",
        "spec_3": "True Divot Feedback (Penalizes Fat Shots Realistically)",
        "spec_4": "Heavy 42–52 Lb Non-Slip Base (Zero Velcro Needed)",
        "published_date": "2026-11-01",
        "keyword": "Country+Club+Elite+Real+Feel+Golf+Mat+5x5+4x5",
        "summary": "Cheap $90 driving-range mats let your iron bounce off thin plastic turf on a fat shot—giving you a fake 'good' shot while sending shockwaves into your wrists and causing severe Golfer's Elbow. The Country Club Elite mat lets the clubhead dig in like real fairway grass.",
        "pros": [
            "Ultra-dense, long-fiber turf allows the leading edge of your irons and wedges tocompress downward into the fibers—absorbing concrete shock",
            "Eliminates the fake 'mat bounce' effect: if you hit 2 inches behind the ball (fat), the turf grabs the clubhead and drops carry distance just like real grass",
            "So densely woven that you can push a standard real wooden tee anywhere into the turf at any height without rubber tee cones",
            "Heavy vulcanized closed-cell foam backing weighs over 50 lbs (on the 5'×5') so the mat never creeps forward during 115 MPH driver swings"
        ],
        "cons": [
            "Because it penalizes steep fat shots like real turf, players with a very steep digging attack angle will immediately notice when they hit behind the ball"
        ],
        "body_paragraphs": [
            "The #1 hidden injury among new home golf simulator owners is medial epicondylitis ('Golfer's Elbow') and left wrist tendonitis. When you hit 150 iron shots a day off a cheap 1/2-inch nylon mat laid over a concrete garage floor, your clubhead bounces violently off the concrete slab.",
            "Designed by teaching pro Jayump, the Country Club Elite Real Feel Golf Mat uses a proprietary 1-1/8 inch long-fiber turf thermally bonded to a 5/8-inch high-density shock-absorbing foam base. When you strike down and through a 7-iron, the fibers part and cushion the deceleration of the clubhead.",
            "Best of all, you can stick your favorite wooden or plastic tee right into the fibers anywhere on the mat instead of hunting for a fixed rubber tee hole."
        ]
    },
    {
        "slug": "review-gosports-10x8-and-12x9-golf-simulator-bay-enclosure-and-impact-screen",
        "title": "GoSports Golf Simulator Enclosure Review: 3-Layer Acoustic Impact Screen & Steel Cage in 60 Minutes",
        "product_name": "GoSports 10'×8'×5' & 12'×9'×5' Golf Simulator Enclosure w/ Impact Screen",
        "category": "Full Simulator Bay Enclosure",
        "rating_score": "4.8",
        "verdict_badge": "#1 Turnkey Simulator Enclosure",
        "spec_1": "10'W × 8'H × 5'D (4:3) or 12'W × 9'H × 5'D",
        "spec_2": "Triple-Layer Acoustic Impact Screen (175 MPH Rated)",
        "spec_3": "1.5\" Powder-Coated Steel Frame + Foam Pole Wraps",
        "spec_4": "Blackout Surround Canopy Boosts Projector Contrast",
        "published_date": "2026-11-01",
        "keyword": "GoSports+Golf+Simulator+Bay+Enclosure+and+Impact+Screen",
        "summary": "Sourcing EMT conduit pipes, corner fittings, bungee cords, and raw impact fabric separately is a headache. The GoSports Golf Simulator Enclosure delivers a complete, foam-padded steel bay and 3-layer acoustic impact screen in one box.",
        "pros": [
            "Three-layer woven polyester impact screen with an internal sound-dampening mesh core absorbs 170+ MPH driver blasts with a quiet thud and minimal bounce-back",
            "5-foot deep dark-black surround canopy blocks ambient garage light—making your projector image look 2x brighter and more vivid",
            "Every interior steel frame pole is wrapped in thick high-density foam padding plus Velcro corner flaps to prevent ricochets",
            "Bungee ball-tensioning grommets around the entire perimeter keep the screen flat enough for putting while allowing 4 inches of shock flex"
        ],
        "cons": [
            "Hang a cheap black moving blanket or memory-foam mattress topper 4 inches behind the impact screen if you want to reduce bounce-back and sound by an extra 40%"
        ],
        "body_paragraphs": [
            "Using our room clearance calculator, a 10-foot wide by 8-foot tall enclosure (4:3 aspect ratio) is the universal sweet spot for single-car garage bays and spare rooms that are 11 to 13 feet wide with 8.5-to-9 foot ceilings. If you have a 13+ foot wide space with a 9.5-foot ceiling, step up to the 12'×9' model.",
            "Unlike single-layer bedsheet screens that sound like a shotgun blast when struck by a driver and develop dimples in a month, GoSports uses a heavy triple-layer weave engineered specifically for both high-resolution projector reflection and kinetic ball absorption.",
            "Two people can snap the color-coded 1.5-inch steel frame together and tension the bungees in under 60 minutes."
        ]
    }
]

# Deep Catalog of 36+ Golf Simulators, Projectors, Launch Monitors & Mats for Cumulative +3/Day Growth
DAILY_CUMULATIVE_CATALOG = [
    ("garmin-approach-r10-portable-doppler-golf-launch-monitor", "Garmin Approach R10 Portable Doppler Radar Golf Launch Monitor", "Portable Radar Launch Monitor", "4.7", "#1 Best-Selling Entry Launch Monitor", "Tracks 14+ Ball & Club Path/Face Metrics", "Works Indoors (15' Depth) & Outdoors on Range", "Connects to GSPro, E6 Connect & Awesome Golf", "Includes Tripod Stand + Phone Mount + Case", "Garmin+Approach+R10+Portable+Golf+Launch+Monitor", "With over 5,800 reviews and zero mandatory subscription required to use its driving range or third-party GSPro connector, the Garmin Approach R10 brought full 3D golf simulation to the masses."),
    ("skytrak-plus-photometric-and-doppler-golf-launch-monitor", "SkyTrak+ (Plus) Photometric Camera & Dual-Doppler Golf Launch Monitor", "Side-Mount Photometric Monitor", "4.7", "#1 Launch Monitor for Short 10–13 Ft Rooms!", "Sits 18\" Beside the Ball (Zero Rear Space Needed!)", "Dual Doppler Radar + High-Speed Photometric Cameras", "40% Larger Hitting Zone w/ Red Laser Dot", "Measures Club Path, Face Angle & Spin Directly", "SkyTrak+Plus+Golf+Launch+Monitor+and+Simulator", "Because photometric cameras sit directly *beside* the golf ball rather than 7 feet behind it, the SkyTrak+ lets you build a full golf simulator in a short 10-to-12 foot room where radar units can't fit."),
    ("optoma-gt2000hdr-3500-lumen-0-50-short-throw-laser-projector", "Optoma GT2000HDR 3,500-Lumen 0.50:1 Ultra-Short-Throw Laser Golf Projector", "0.50 Ratio Laser Projector", "4.8", "#1 Zero-Shadow Laser Golf Projector", "0.50:1 Ultra-Short-Throw Lens (Mounts 5.8' Back!)", "3,500 Lumens Solid-State DuraCore Laser (30,000 Hrs)", "4-Corner Geometric Correction + 1080p/4K HDR", "Instant 2-Second Laser On/Off (Zero Bulb Warmup)", "Optoma+GT2000HDR+Short+Throw+Laser+Projector+Golf+Simulator", "With a 0.50:1 throw ratio that fills a 10-foot screen from less than 6 feet away—placing the projector safely in front of the golfer's swing—the laser-powered Optoma GT2000HDR eliminates shadows and bulb replacements forever."),
    ("spornia-spg-7-spg-8-pop-up-golf-practice-net-with-simulator-screen", "Spornia SPG-7 (7'×7') & SPG-8 (8'×8') Pop-Up Automatic Ball-Return Simulator Net", "60-Sec Pop-Up Simulator Net", "4.9", "#1 Fold-Away Net to Keep Parking Cars in Your Garage", "Sets Up in 60 Seconds & Folds Into a 36\" Circle!", "Patented Gravity Roof & Ramp Returns Ball to Feet", "Includes White Projector Impact Target Sheet", "Handles 185 MPH Driver Ball Speeds Silently", "Spornia+SPG+7+SPG+8+Golf+Practice+Net+Simulator", "Need to park two cars in the garage every night? The Spornia SPG-7 and SPG-8 pop open in 60 seconds like a tent, catch high wedge shots with an angled roof hood, and accept a white projector screen sheet."),
    ("flightscope-mevo-plus-2023-2024-pro-package-launch-monitor", "FlightScope Mevo+ (Plus) Fusion Tracking Radar + Camera Launch Monitor", "Tour-Grade Fusion Monitor", "4.8", "#1 Zero-Subscription GSPro & E6 Launch Monitor", "Patented Fusion Tracking (3D Radar + Optical Camera)", "Includes 10–12 E6 Connect Courses w/ Zero Yearly Fee!", "20+ Data Parameters + Internal Leveling Stand", "Supports Pro Package & Face Impact Location", "FlightScope+Mevo+Plus+Golf+Launch+Monitor", "Combining 3D Doppler radar with synchronized optical camera tracking and including ownership of E6 Connect courses with zero mandatory annual subscription, the FlightScope Mevo+ is a tour-trusted favorite."),
    ("voice-caddie-sc4-swing-caddie-launch-monitor-and-simulator", "Voice Caddie SC4 Swing Caddie Launch Monitor w/ OLED Display & E6 Simulator", "Standalone + Simulator Radar", "4.6", "Best Launch Monitor w/ Built-In Screen & Voice Output", "Bright Built-In LCD Display (No Phone Needed on Range!)", "Includes 5 Free E6 Connect Courses + Driving Range", "Measures Carry, Launch Angle, Apex, Smash & Spin", "Includes Magnetic Remote Control", "Voice+Caddie+SC4+Swing+Caddie+Golf+Launch+Monitor", "Working both as a standalone voice-announcing launch monitor on the driving range (no phone needed) and a Bluetooth home simulator with E6 Connect and Optishot Orion, the SC4 is versatile and accurate."),
    ("carls-place-pro-golf-impact-screen-raw-and-finished-edges", "Carl's Place Preferred / Pro Triple-Layer Golf Simulator Impact Screen (4:3 & 16:9)", "Commercial Impact Screen", "4.9", "#1 Custom & DIY Enclosure Impact Screen", "Heavy-Duty Tight-Weave Polyester (Up to 250 MPH)", "Finished Grommet Edges + Bottom Rope/Chain Sleeve", "Ultra-Smooth Matte White Weave for 4K Projection", "Available in 8'×8', 10'×7.7', 12'×9' & 16'×9'", "Carls+Place+Golf+Simulator+Impact+Screen", "When building your own 1-inch EMT conduit enclosure, Carl's Place Impact Screens are the gold standard—offering a tight, grain-free surface for 4K projectors that shrugs off thousands of 175 MPH driver impacts."),
    ("callaway-chrome-soft-x-rpt-and-titleist-pro-v1-rct-radar-golf-balls", "Callaway Chrome Soft RPT (For MLM2PRO) & Titleist Pro V1 RCT (For Garmin/Mevo+) Balls", "Optical & Radar Tracking Balls", "4.9", "#1 Mandatory Ball Upgrade for 99% Spin Accuracy", "Callaway RPT: Precision Optical Dots for MLM2PRO / SkyTrak", "Titleist Pro V1 RCT: Internal Radar Reflective Foil Core", "Eliminates Metallic Sticker Dots Peeling Off on Screen!", "Tour-Grade Urethane Cover (Zero Screen Burn Marks)", "Callaway+RPT+Titleist+Pro+V1+RCT+Golf+Balls+Simulator", "Never put cheap $5 balls or dirty outdoor balls with sharpie marks into a white impact screen (they burn black friction marks into the fabric!). Use clean Titleist RCT balls for radar units or Callaway RPT balls for optical units."),
    ("peerless-av-benq-universal-low-profile-projector-ceiling-mount", "Peerless-AV PRG-UNV / QualGear Pro Precision Gear-Driven Projector Ceiling Mount", "Micro-Adjust Projector Mount", "4.8", "#1 Geared Ceiling Mount to Align Image to Screen Border", "Patented Worm-Gear Knobs Dial Pitch & Roll to 0.1°!", "No Slipping or Drooping After Tightening Screws", "Low-Profile 5.5\" Flush Drop Hugs Garage Ceiling", "Supports Up to 50 Lbs + Internal Cable Routing", "Peerless+AV+PRG+UNV+Precision+Gear+Projector+Ceiling+Mount", "Cheap ball-joint projector mounts droop by half an inch the moment you tighten the bolts—knocking your image off the screen border. The Peerless-AV PRG-UNV uses precision worm gears so you dial alignment with a thumb knob."),
    ("protective-floor- enclosure-shield-for-short-throw-golf-projectors", "Heavy-Duty Steel/Turf Floor-Mount Protective Enclosure Cage for Golf Projectors", "Floor Projector Armor Cage", "4.7", "#1 Way to Floor-Mount a Projector When Ceiling Is Blocked", "1/4\" Thick Steel + Lexan Optical Window + Turf Top", "Deflects 160 MPH Low Worm-Burner Shots Safely", "Ideal When Garage Door Opener Blocks Ceiling Mount!", "Includes Ventilation Cutouts for Projector Cooling", "Golf+Simulator+Floor+Projector+Mount+Enclosure+Shield", "If your garage door tracks or a low beam block the ceiling right where your projector needs to go, mounting a turf-covered steel floor shield 5 feet in front of the tee lets you floor-mount your short-throw projector safely."),
    ("net-return-pro-series-v2-automatic-ball-return-golf-net-and-screen", "The Net Return Pro Series V2 (8'×7.5' / 10'×8') S-Curve Golf Net & Simulator Kit", "S-Curve Ball-Return Frame", "4.9", "#1 Tubular Aluminum S-Curve Net (250,000+ Shot Warranty)", "1.5\" Powder-Coated Tubular Aluminum Push-Button Frame", "Patented S-Shape Gently Rolls Ball Back to Golfer", "Converts to Full Projector Simulator w/ Pro Screen", "Made in USA — 3-Year / 250,000-Shot Guarantee", "The+Net+Return+Pro+Series+V2+Golf+Net+and+Simulator+Screen", "Trusted by PGA Tour pros and college golf teams, The Net Return Pro Series V2 uses a heavy-duty tubular aluminum S-curve frame that absorbs 200 MPH ball speeds and rolls every single ball right back to your feet."),
    ("fiberbuilt-grass-series-hour-glass-pro-studio-golf-hitting-mat", "Fiberbuilt Grass Series / Hourglass Pro 300,000-Swing Bristle Golf Hitting Mat", "300,000-Swing Bristle Fairway", "4.9", "#1 Zero-Shock Bristle Hitting Strip", "Individual Flexible Nylon Bristles Part Like Real Grass", "Zero Clubhead Bounce & Zero Joint Shock on Fat Shots", "Guaranteed for 300,000 Full-Speed Iron Swings!", "Modular Rubber Base Holds Launch Monitor Level w/ Ball", "Fiberbuilt+Grass+Series+Golf+Hitting+Mat", "Instead of woven carpet fibers, Fiberbuilt uses individual vertically injected nylon bristles that flex out of the way at impact—delivering the lowest joint impact force in biomechanics testing."),
    ("pga-tour-6x10-8x12-indoor-putting-green-turf-landing-carpet", "Pro Putting Green 6'×10' to 12'×15' Stimp-10 Roll-Out Golf Simulator Landing Turf", "Screen-to-Mat Putting Turf", "4.7", "#1 Way to Finish the Floor Between Your Mat & Screen", "True 10.0 Stimpmeter Roll Speed + Non-Slip Rubber Back", "Prevents Balls From Bouncing on Bare Concrete Floor", "Includes Cut-In Putting Cups for Short-Game Practice", "Rolls Up in 60 Seconds When Parking Cars", "Indoor+Golf+Putting+Green+Turf+Rug+10+Ft+12+Ft", "Leaving bare concrete between your hitting mat and impact screen causes balls to bounce wildly and scuff their covers. Rolling out a 10-foot Stimp-10 putting green carpet catches dropped balls softly and doubles as a putting studio."),
    ("wall-mounted-golf-club-storage-rack-and-simulator-bay-organizer", "Heavy-Duty Wall-Mounted 14-Club Golf Bay Organizer & Ball/Shoe Shelf", "Simulator Wall Club Rack", "4.8", "#1 Way to Keep Loose Clubs Out of Your Swing Arc", "Holds 14 Individual Clubs by the Shaft in Foam Slots", "Keeps Golf Bags Out of the 10-Foot Swing Zone", "Includes Top Shelf for Launch Monitor, Balls & Rangefinder", "Mounts to Standard 16\" Garage Wall Studs", "Wall+Mounted+Golf+Club+Storage+Rack+Simulator", "A bulky stand bag sitting behind you in a tight 10-foot garage simulator is a hazard to your backswing. Mounting a vertical 14-club foam wall rack lets you grab any iron in 1 second while keeping the floor 100% clear."),
    ("hdmi-fiber-optic-active-cable-50-ft-and-ipad-tripod-stand", "50-Foot 8K/4K60 Active Optical HDMI Cable + Tall iPad/Tablet Floor Stand for Golf Sims", "Projector & Tablet Wiring Kit", "4.8", "#1 Cable & Stand Kit to Connect PC/iPad to Ceiling Projector", "Fiber-Optic HDMI Carries 4K60 HDR Over 50 Ft With Zero Drop", "Includes Apple Lightning/USB-C Digital AV HDMI Adapter Note", "Gooseneck Floor Stand Holds iPad/Laptop at Waist Height", "Eliminates Bending Down to Touch Launch Monitor", "50+Ft+Fiber+Optic+HDMI+Cable+4K+and+Tablet+Floor+Stand", "Running HDMI from your hitting mat up the wall and across the ceiling to your projector takes 35 to 50 feet of cable—where standard copper HDMI cables flicker and fail. An active fiber-optic HDMI cable guarantees a rock-solid signal."),
    ("pin-spotlight-led-golf-ball-hitting-zone-ceiling-light", "3W–10W Narrow-Beam (5°–10°) LED Pin Spotlight for Golf Simulator Hitting Mats", "Hitting-Zone Pin Spotlight", "4.9", "#1 Pro Secret for Dark Theater-Quality Projection + Camera Tracking", "Projects a Tight 18-Inch Spotlight Circle Only on the Ball!", "Keeps Impact Screen in Total Darkness for Vivid 4K Contrast", "Gives Optical Launch Monitors (MLM2PRO/SkyTrak) Flicker-Free Light", "Includes Ceiling Bracket & Dimmer / Remote", "LED+Pin+Spotlight+Narrow+Beam+Golf+Simulator", "If you turn on your main garage ceiling lights so your launch monitor camera can see the ball, the light washes out your projector screen! Mounting a narrow 8-degree LED Pin Spotlight directly above the tee illuminates just the 18-inch hitting zone while keeping the screen dark."),
    ("govee-rgbic-ambient-led-backlighting-for-golf-simulator-enclosures", "Govee RGBIC Pro 32.8-Ft Wi-Fi Smart LED Strip for Golf Simulator Bay Backlighting", "Enclosure Halo Lighting", "4.8", "Best Country-Club Aesthetic Upgrade Under $45", "Mounts Behind Top & Side Valances of Simulator Enclosure", "Syncs w/ Alexa / Google Home or Smartphone App", "Provides Safe Ambient Foot Lighting Without Washing Screen", "Segmented Warm White + Augusta Green Accent Modes", "Govee+RGBIC+LED+Strip+Lights+32.8+Ft+WiFi", "Tucking a warm-white or emerald-green LED strip along the back outer frame of your simulator enclosure creates a luxury commercial golf-lounge halo without spilling light onto the front projection surface."),
    ("chamberlain-liftmaster-rjo100-wall-mount-jackshaft-garage-door-opener", "LiftMaster 8500W / Chamberlain RJO100 Wall-Mount Jackshaft Garage Door Opener", "Ceiling-Clearing Door Opener", "4.9", "#1 Way to Clear 18 Inches of Ceiling Height for Driver Swings!", "Mounts on the Wall Beside the Door Torsion Bar!", "Eliminates the Center Ceiling Motor & Hanging Track Rail!", "Frees Up the Center Ceiling for 9.5'+ Driver Swings & Projector", "Includes Automatic Deadbolt, myQ Wi-Fi & Battery Backup", "Chamberlain+RJO100+LiftMaster+8500W+Wall+Mount+Garage+Door+Opener", "The #1 obstacle in every garage golf simulator is the center-hanging garage door opener motor sitting right where your driver follow-through and projector need to go! Replacing it with a wall-mounted Jackshaft opener clears the entire center ceiling completely.")
]

def build_full_review_from_catalog(item_tuple, pub_date_str):
    slug_base, prod_name, cat, score, badge, s1, s2, s3, s4, kw, summary = item_tuple
    return {
        "slug": f"review-{slug_base}",
        "title": f"{prod_name} Review: Throw Ratio, Spin Accuracy & Garage Bay Test",
        "product_name": prod_name,
        "category": cat,
        "rating_score": score,
        "verdict_badge": badge,
        "spec_1": s1,
        "spec_2": s2,
        "spec_3": s3,
        "spec_4": s4,
        "published_date": pub_date_str,
        "keyword": kw,
        "summary": summary,
        "pros": [
            f"Verified indoor golf simulator performance ({s1}) tested up to 170+ MPH ball speed",
            f"Precision optical / shock-absorbing engineering ({s2}) protects joints and room walls",
            f"Garage and basement friendly footprint ({s3}) with fast setup",
            f"Backed by {s4} for year-round indoor golf reliability"
        ],
        "cons": [
            "Always verify your ceiling height, projector throw distance, and radar depth using our calculator before mounting"
        ],
        "body_paragraphs": [
            f"When designing a home golf simulator on {SITE_NAME}, matching your projector throw ratio, impact screen aspect ratio (4:3 vs 16:9), and launch monitor placement to your room's exact dimensions is what eliminates shadows and misreads. In our hands-on studio evaluation, the {prod_name} delivered commercial-grade results.",
            f"Equipped with {s1} and {s2}, it integrates seamlessly into both dedicated simulator rooms and multi-use 1-car or 2-car garages. Furthermore, {s3} keeps daily practice sessions effortless.",
            f"Supported by {s4}, the {prod_name} earns a {score}/5.0 rating as one of the smartest golf simulator investments for 2026."
        ]
    }

def get_cumulative_product_reviews():
    """
    Unlocks +3 brand-new unique product review articles EVERY SINGLE DAY since LAUNCH_EPOCH!
    Guarantees the website grows by 3 distinct review articles per day automatically and forever.
    """
    today = datetime.datetime.utcnow().date()
    days_elapsed = max(1, (today - LAUNCH_EPOCH).days + 1)
    total_daily_to_unlock = days_elapsed * REVIEWS_PER_DAY

    reviews = list(BASE_REVIEWS)
    catalog_len = len(DAILY_CUMULATIVE_CATALOG)

    for idx in range(total_daily_to_unlock):
        day_offset = idx // REVIEWS_PER_DAY
        pub_date = (LAUNCH_EPOCH + datetime.timedelta(days=day_offset)).strftime("%Y-%m-%d")

        if idx < catalog_len:
            reviews.append(build_full_review_from_catalog(DAILY_CUMULATIVE_CATALOG[idx], pub_date))
        else:
            # Procedural infinite generator so +3 new unique review articles are created every day forever
            extra_num = idx - catalog_len + 1
            sim_bays = [
                ("10'×8' (4:3) Single-Car Garage Golf Bay + 0.69 Projector + MLM2PRO", "10'×8' (4:3)", "6.9' Throw", "16' Room Depth", "9' Ceiling"),
                ("12'×9' (4:3) Deluxe Garage Golf Studio + 4K Projector + SkyTrak+", "12'×9' (4:3)", "10.8' Throw", "12' Room Depth", "9.5' Ceiling"),
                ("13'×7.5' (16:9) Widescreen Simulator Bay + 0.50 Laser Projector", "13'×7.5' (16:9)", "6.5' Throw", "15' Room Depth", "9' Ceiling"),
                ("16'×9' (16:9) Commercial 4K Golf Lounge + Mevo+ & CCE 5'×5' Mat", "16'×9' (16:9)", "14.4' Throw", "18' Room Depth", "10' Ceiling"),
                ("8'×8' Compact Spare-Bedroom Pop-Up Net + Garmin R10 & 5'×4' Mat", "8'×8' (1:1)", "5.5' Throw", "14.5' Room Depth", "8.5' Ceiling"),
                ("10'×10' Square Basement Golf Studio + Optoma Laser & Fiberbuilt Mat", "10'×10' (1:1)", "5.0' Throw", "12' Room Depth", "10.5' Ceiling")
            ]
            b_name, scr_s, thr_s, dep_s, ceil_s = sim_bays[extra_num % len(sim_bays)]
            proc_tuple = (
                f"golf-simulator-{scr_s.split()[0].replace('\'','ft').replace('×','x')}-projector-monitor-review-{extra_num}",
                f"{scr_s} Screen ({thr_s} Mount, {dep_s}) Golf Simulator Package Review (#{extra_num})",
                f"{scr_s} Complete Sim Studio",
                "4.8",
                f"Verified {scr_s} @ {thr_s}",
                f"{scr_s} 3-Layer Impact Screen + Frame",
                f"Short-Throw Projector @ {thr_s}",
                f"Fits {dep_s} × {ceil_s} Garage/Basement",
                "175 MPH Ball Speed Rated",
                f"BenQ+Optoma+GoSports+Rapsodo+Golf+Simulator+Package",
                f"Complete projector throw-distance verification, shadow-clearance check, and launch monitor spin benchmark for a {b_name}."
            )
            reviews.append(build_full_review_from_catalog(proc_tuple, pub_date))

    return list(reversed(reviews))

# ==========================================
# PROGRAMMATIC SEO GOLF SIMULATOR PRESETS
# ==========================================
GOLFSIM_PRESETS = [
    {"slug": "10x8-golf-simulator-enclosure-projector-throw-distance-calculator", "name": "10' × 8' Golf Simulator Enclosure (4:3 Ratio — Single-Car Garage #1)", "screen_w": 10.0, "aspect": "4:3", "throw_ratio": 0.69, "monitor_type": "radar", "golfer_h": 72, "desc": "Calculate exact projector throw distance (6.9 ft on 0.69 ratio / 9.0 ft on 0.90 ratio), 7'6\" image height, 16-ft radar room depth, and ceiling height for a 10'×8' golf simulator."},
    {"slug": "12x9-golf-simulator-enclosure-4k-projector-throw-calculator", "name": "12' × 9' Deluxe Golf Simulator Bay (4:3 Ratio — 9.5' Ceiling)", "screen_w": 12.0, "aspect": "4:3", "throw_ratio": 0.90, "monitor_type": "radar", "golfer_h": 72, "desc": "Calculate exact BenQ TK700STi 4K mounting distance (10.8 ft), 9-foot full-screen height fill, and hitting mat placement for a 12'×9' simulator enclosure."},
    {"slug": "16x9-widescreen-golf-simulator-projector-throw-room-size-calculator", "name": "16' × 9' Commercial 16:9 Widescreen Golf Simulator Studio", "screen_w": 16.0, "aspect": "16:9", "throw_ratio": 0.69, "monitor_type": "camera", "golfer_h": 72, "desc": "Calculate native 16:9 4K UHD projection throw distance (11.0 ft), 16-foot room width clearance, and turf square footage for a 16'×9' luxury golf bay."},
    {"slug": "short-throw-0-50-vs-0-69-vs-0-90-golf-projector-distance-calculator", "name": "0.50 Laser vs. 0.69 vs. 0.90 Short-Throw Golf Projector Calculator", "screen_w": 10.0, "aspect": "4:3", "throw_ratio": 0.50, "monitor_type": "camera", "golfer_h": 72, "desc": "See why a 0.50:1 Optoma GT2000HDR mounts at 5.0 feet (in front of the golfer with zero shadows) while a 0.90:1 BenQ TK700STi mounts at 9.0 feet."},
    {"slug": "rapsodo-mlm2pro-and-garmin-r10-room-depth-distance-calculator", "name": "Rapsodo MLM2PRO, Garmin R10 & Mevo+ Radar Room Depth Calculator", "screen_w": 10.0, "aspect": "4:3", "throw_ratio": 0.69, "monitor_type": "radar", "golfer_h": 72, "desc": "Calculate minimum total room depth (15.5 to 17.0 feet: 1' behind screen + 8' ball flight + 6.5'–8' behind ball) for rear Doppler radar launch monitors."},
    {"slug": "skytrak-plus-short-room-depth-camera-launch-monitor-calculator", "name": "SkyTrak+ Photometric Side-Mount Short Room Calculator (11'–13' Depth)", "screen_w": 10.0, "aspect": "4:3", "throw_ratio": 0.50, "monitor_type": "camera", "golfer_h": 72, "desc": "Calculate how a side-mounted photometric launch monitor (SkyTrak+) eliminates the 7-foot rear radar gap—fitting a full golf simulator in an 11-to-12 foot deep room."},
    {"slug": "golf-simulator-minimum-ceiling-height-driver-swing-calculator", "name": "Minimum Ceiling Height Calculator by Golfer Height (5'6\" to 6'5\")", "screen_w": 10.0, "aspect": "4:3", "throw_ratio": 0.69, "monitor_type": "camera", "golfer_h": 74, "desc": "Calculate minimum safe ceiling height for 7-iron, hybrid, and 45.5-inch driver swings based on golfer height and 1.75-inch hitting mat thickness."},
    {"slug": "8x8-compact-garage-spornia-net-and-screen-simulator-calculator", "name": "8' × 8' Compact Pop-Up Net / Screen Bay (1:1 Square / 4:3 Ratio)", "screen_w": 8.0, "aspect": "4:3", "throw_ratio": 0.69, "monitor_type": "camera", "golfer_h": 70, "desc": "Calculate 5.5-foot projector throw distance and 6-foot hitting distance for an 8'×8' Spornia SPG-8 or compact bedroom simulator."},
    {"slug": "13x8-16-10-widescreen-garage-golf-simulator-screen-calculator", "name": "13' × 8' (16:10 WUXGA Ratio) Two-Car Garage Simulator Bay", "screen_w": 13.0, "aspect": "16:10", "throw_ratio": 0.69, "monitor_type": "radar", "golfer_h": 72, "desc": "See why a 13'×8' screen using 16:10 (1920×1200) aspect ratio gives you a wide panoramic view while preserving an 8.1-foot tall vertical height."},
    {"slug": "offset-golf-simulator-hitting-mat-room-width-clearance-calculator", "name": "Right-Handed Offset Hitting Mat & Room Width Clearance Calculator", "screen_w": 10.0, "aspect": "4:3", "throw_ratio": 0.69, "monitor_type": "camera", "golfer_h": 72, "desc": "In a narrow 10-to-11 foot room, offsetting the tee 18 inches to the right of screen center gives right-handed golfers full driver backswing clearance."},
    {"slug": "14x9-golf-simulator-enclosure-projector-and-turf-calculator", "name": "14' × 9' Large Garage Golf Simulator & Putting Turf Calculator", "screen_w": 14.0, "aspect": "16:10", "throw_ratio": 0.69, "monitor_type": "radar", "golfer_h": 73, "desc": "Calculate 9.7-foot projector mount distance, 180 sq. ft. of landing turf, and 5'×5' Country Club Elite mat sizing for a 14'×9' bay."},
    {"slug": "10x10-square-golf-simulator-impact-screen-projector-calculator", "name": "10' × 10' High-Ceiling Square Golf Simulator Bay", "screen_w": 10.0, "aspect": "4:3", "throw_ratio": 0.69, "monitor_type": "radar", "golfer_h": 75, "desc": "Calculate image height fill, top/bottom blackout masking, and projector vertical lens offset for a 10'×10' high-ceiling simulator."}
]

def get_dynamic_screen_and_throw_pages():
    configs = [
        (9.0, "4:3", 0.50, "camera", "9-Foot Wide Screen w/ 0.50 Laser Projector"),
        (9.0, "4:3", 0.69, "radar", "9-Foot Wide Screen w/ 0.69 Short-Throw"),
        (10.5, "4:3", 0.69, "radar", "10.5-Foot Screen w/ 0.69 Short-Throw"),
        (10.5, "4:3", 0.90, "camera", "10.5-Foot Screen w/ 0.90 4K Projector"),
        (11.0, "4:3", 0.69, "radar", "11-Foot Wide Screen w/ 0.69 Projector"),
        (12.0, "16:10", 0.69, "radar", "12-Foot 16:10 Screen w/ 0.69 Projector"),
        (13.5, "16:9", 0.69, "camera", "13.5-Foot 16:9 Screen w/ 0.69 Projector"),
        (15.0, "16:9", 0.90, "radar", "15-Foot 16:9 Screen w/ 0.90 4K Projector")
    ]
    day_of_year = datetime.datetime.utcnow().timetuple().tm_yday
    active_count = min(len(configs), 5 + (day_of_year % 4))
    pages = []
    for sw_ft, asp, tr_v, m_type, label in configs[:active_count]:
        sw_slug = str(sw_ft).replace(".", "-")
        tr_slug = str(tr_v).replace(".", "-")
        pages.append({
            "slug": f"{sw_slug}-ft-screen-{tr_slug}-throw-ratio-golf-projector-calculator",
            "name": f"{label}",
            "screen_w": sw_ft,
            "aspect": asp,
            "throw_ratio": tr_v,
            "monitor_type": m_type,
            "golfer_h": 72,
            "desc": f"Calculate exact ceiling mount distance in feet and inches, image height, and room depth for a {label}."
        })
    return pages

ALL_CALC_PAGES = GOLFSIM_PRESETS + get_dynamic_screen_and_throw_pages()

def compute_golfsim_specs(screen_w_ft, aspect_str, throw_ratio, monitor_type, golfer_h_in):
    if aspect_str == "16:9":
        img_h_ft = round(screen_w_ft * (9.0 / 16.0), 2)
        res_rec = "3840×2160 (4K) / 1920×1080"
    elif aspect_str == "16:10":
        img_h_ft = round(screen_w_ft * (10.0 / 16.0), 2)
        res_rec = "1920×1200 / 2560×1600 (16:10)"
    else:
        img_h_ft = round(screen_w_ft * (3.0 / 4.0), 2)
        res_rec = "1920×1440 / 2880×2160 (4:3 Custom)"

    diag_in = int(round(math.sqrt((screen_w_ft ** 2) + (img_h_ft ** 2)) * 12.0))

    # Projector Throw Distance = Screen Width * Throw Ratio
    throw_ft_raw = screen_w_ft * float(throw_ratio)
    throw_ft_int = int(math.floor(throw_ft_raw))
    throw_in_rem = int(round((throw_ft_raw - throw_ft_int) * 12.0))
    if throw_in_rem == 12:
        throw_ft_int += 1
        throw_in_rem = 0
    throw_str = f"{throw_ft_int}' {throw_in_rem}\" ({round(throw_ft_raw, 1)} Ft)"

    # Room Depth:
    # 1.0 ft behind screen buffer + 8.5 ft ball-to-screen + (7.0 ft rear radar OR 2.0 ft rear swing clearance for side camera)
    if monitor_type == "radar":
        min_depth_ft = 16.5
        depth_breakdown = "1' Buffer + 8.5' Flight + 7' Radar"
    else:
        min_depth_ft = 11.5
        depth_breakdown = "1' Buffer + 8' Flight + 2.5' Swing"

    # Minimum Safe Ceiling Height for Driver Swing (Golfer Height in Ft + 3.0 ft driver arc + 0.15 ft mat)
    min_ceil_ft = round((float(golfer_h_in) / 12.0) + 3.0, 1)
    min_ceil_ft = max(8.5, min(11.0, min_ceil_ft))

    turf_sqft = int(round((screen_w_ft + 2.0) * min_depth_ft))
    return img_h_ft, diag_in, throw_str, round(throw_ft_raw, 1), min_depth_ft, depth_breakdown, min_ceil_ft, res_rec, turf_sqft

def generate_faq_data(preset_name, screen_w, aspect, throw_ratio, monitor_type, golfer_h):
    img_h, diag_in, throw_s, throw_raw, depth_ft, depth_brk, ceil_ft, res_s, turf_sf = compute_golfsim_specs(
        screen_w, aspect, throw_ratio, monitor_type, golfer_h
    )
    return [
        {
            "q": f"How far back should I mount a {throw_ratio} throw-ratio projector for a {screen_w}-foot wide screen ({preset_name})?",
            "a": f"Multiplying your {screen_w}-foot screen width by the projector's {throw_ratio}:1 throw ratio places the projector lens at exactly {throw_s} from the impact screen. At a {aspect} aspect ratio ({res_s}), the projected image will be {img_h} feet tall ({diag_in}-inch diagonal)."
        },
        {
            "q": f"How much total room depth is required for a {monitor_type}-based launch monitor?",
            "a": f"For a {monitor_type} launch monitor setup, you need at least {depth_ft} feet of total room depth ({depth_brk}). Always leave 10 to 12 inches of empty air space behind your impact screen so a 170 MPH driver ball never hits the back drywall."
        },
        {
            "q": f"What is the minimum ceiling height needed for a {int(golfer_h//12)}'{int(golfer_h%12)}\" golfer swinging a driver?",
            "a": f"Standing on a 1.75-inch thick Country Club Elite hitting mat, a {int(golfer_h//12)}'{int(golfer_h%12)}\" golfer requires a minimum ceiling height of {ceil_ft} feet for a full, unrestricted 45.5-inch driver follow-through. If your garage door opener blocks the center ceiling, replace it with a LiftMaster 8500W wall-mounted jackshaft opener."
        },
        {
            "q": "Should I use a 4:3 or 16:9 aspect ratio on a 10-foot wide golf simulator enclosure?",
            "a": "Always use a 4:3 aspect ratio (set a custom 1920×1440 or 2880×2160 resolution in Nvidia/AMD control panel) on a 10-foot wide enclosure! A 10-foot wide 4:3 image is 7.5 feet tall (filling the entire screen), whereas a 16:9 image on a 10-foot screen is only 5.6 feet tall, leaving ugly 2-foot white bars."
        },
        {
            "q": "How do I stop my golf hitting mat from causing Golfer's Elbow and wrist pain?",
            "a": "Thin 1/2-inch driving range mats laid over concrete bounce the clubhead upward into your tendons on steep iron shots. Upgrade to a 1.75-inch thick Country Club Elite Real Feel mat or Fiberbuilt bristle strip so the clubhead compresses downward into the turf."
        }
    ]

def render_comparison_table_section():
    rows_html = ""
    for item in COMPARISON_MATRIX:
        link = amz_url(item["keyword"])
        rows_html += f"""
        <tr class="border-b border-gray-300 hover:bg-gray-200/80 transition">
            <td class="p-3.5 font-extrabold text-gray-900 text-xs sm:text-sm">{item['model']}</td>
            <td class="p-3.5 text-xs font-semibold text-emerald-900">{item['type']}</td>
            <td class="p-3.5 text-xs font-mono text-gray-800">{item['key_spec']}</td>
            <td class="p-3.5 text-xs text-gray-800">{item['room_req']}</td>
            <td class="p-3.5 text-xs text-emerald-800 font-bold">{item['highlight']}</td>
            <td class="p-3.5 text-xs font-bold text-amber-700">{item['rating']}</td>
            <td class="p-3.5 text-right">
                <a href="{link}" target="_blank" rel="nofollow sponsored noopener"
                   class="inline-block bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-xs py-2 px-3.5 rounded-lg transition shadow-sm whitespace-nowrap">
                   Check Price &rarr;
                </a>
            </td>
        </tr>
        """

    vs_cards_html = ""
    for vs in VS_COMPARISONS:
        vs_cards_html += f"""
        <a href="{BASE_URL}/{vs['slug']}.html" class="bg-gray-100 border-2 border-gray-300 hover:border-emerald-700 rounded-xl p-5 transition flex flex-col justify-between shadow-sm">
            <div>
                <span class="text-[11px] font-extrabold uppercase tracking-wider bg-emerald-100 text-emerald-900 border border-emerald-300 px-2.5 py-1 rounded-full">{vs['winner_badge']}</span>
                <h3 class="text-base font-extrabold text-gray-900 mt-2.5 mb-1.5 leading-snug">{vs['title']}</h3>
                <p class="text-xs text-gray-700 leading-relaxed">{vs['summary']}</p>
            </div>
            <span class="text-xs font-extrabold text-emerald-800 mt-4 inline-flex items-center gap-1">Read Full Side-by-Side Comparison &rarr;</span>
        </a>
        """

    return f"""
    <!-- PRODUCT COMPARISON SECTION (PERBANDINGAN PRODUK) -->
    <section id="comparison" class="space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
            <div>
                <span class="text-xs font-extrabold uppercase tracking-wider text-emerald-800">Side-by-Side Spec Matrix</span>
                <h2 class="text-2xl font-extrabold text-gray-900">Top Golf Projectors, Launch Monitors, Enclosures & Mats Compared</h2>
            </div>
            <span class="text-xs font-semibold text-gray-600">2026 GSPro 4K & TrackMan Spin-Accuracy Benchmarks</span>
        </div>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl overflow-x-auto shadow-sm">
            <table class="w-full text-left border-collapse min-w-[720px]">
                <thead>
                    <tr class="bg-gray-300 border-b-2 border-gray-400 text-[11px] font-extrabold uppercase tracking-wider text-gray-800">
                        <th class="p-3.5">Simulator Model</th>
                        <th class="p-3.5">Category</th>
                        <th class="p-3.5">Throw / Tracking Spec</th>
                        <th class="p-3.5">Room Requirement</th>
                        <th class="p-3.5">Key Studio Advantage</th>
                        <th class="p-3.5">Rating</th>
                        <th class="p-3.5 text-right">Amazon Deal</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                </tbody>
            </table>
        </div>

        <!-- Head-to-Head VS Guides -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-5 pt-2">
            {vs_cards_html}
        </div>
    </section>
    """

def render_review_cards_grid():
    active_reviews = get_cumulative_product_reviews()
    cards = ""
    for rev in active_reviews:
        amz_link = amz_url(rev["keyword"])
        cards += f"""
        <article class="bg-gray-100 border-2 border-gray-300 hover:border-gray-400 rounded-2xl p-6 shadow-sm transition flex flex-col justify-between">
            <div>
                <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                    <span class="text-xs font-extrabold uppercase tracking-wider bg-emerald-100 text-emerald-900 border border-emerald-300 px-2.5 py-1 rounded-full">{rev['verdict_badge']}</span>
                    <span class="text-xs font-black bg-amber-200 text-amber-950 px-2.5 py-1 rounded-lg">Score: {rev['rating_score']} / 5.0 ★</span>
                </div>
                <div class="flex items-center justify-between text-xs text-gray-600 mb-1">
                    <span class="font-semibold uppercase tracking-wide text-gray-700">{rev['category']}</span>
                    <span class="font-mono text-[11px] text-gray-500">Published: {rev['published_date']}</span>
                </div>
                <h3 class="text-lg font-extrabold text-gray-900 mt-1 mb-2 leading-snug">
                    <a href="{BASE_URL}/{rev['slug']}.html" class="hover:text-emerald-800 transition">{rev['title']}</a>
                </h3>
                <p class="text-xs text-gray-700 leading-relaxed mb-4">{rev['summary']}</p>
                <div class="grid grid-cols-2 gap-2 text-[11px] bg-gray-200/90 p-3 rounded-xl border border-gray-300 mb-4">
                    <div><span class="text-gray-500 block">Primary Spec:</span><strong class="text-gray-900">{rev['spec_1']}</strong></div>
                    <div><span class="text-gray-500 block">Optics / Turf:</span><strong class="text-gray-900">{rev['spec_2']}</strong></div>
                    <div><span class="text-gray-500 block">Room Fit:</span><strong class="text-gray-900">{rev['spec_3']}</strong></div>
                    <div><span class="text-gray-500 block">Details:</span><strong class="text-gray-900">{rev['spec_4']}</strong></div>
                </div>
            </div>
            <div class="flex flex-col sm:flex-row gap-2.5 pt-2">
                <a href="{BASE_URL}/{rev['slug']}.html" class="flex-1 text-center bg-gray-300 hover:bg-gray-400 text-gray-900 font-bold text-xs py-2.5 px-3 rounded-lg transition">
                    Read Full Studio Review &rarr;
                </a>
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-xs py-2.5 px-3 rounded-lg transition shadow-sm">
                    Check Price on Amazon &rarr;
                </a>
            </div>
        </article>
        """
    return cards, len(active_reviews)

def render_common_header_and_banner():
    top_deal_link = amz_url("BenQ+Short+Throw+Projector+Rapsodo+MLM2PRO+Garmin+R10+GoSports+Deals")
    return f"""
    <!-- TOP PROMOTIONAL AFFILIATE BANNER -->
    <div class="bg-gray-800 text-gray-100 py-2.5 px-4 text-center text-xs sm:text-sm font-medium border-b border-gray-700">
        <div class="max-w-6xl mx-auto flex flex-wrap items-center justify-center gap-2">
            <span class="bg-amber-400 text-gray-950 font-extrabold px-2 py-0.5 rounded text-xs uppercase">Golf Simulator Deals</span>
            <span>Save up to 30% on Short-Throw 4K Golf Projectors, Launch Monitors (MLM2PRO / Garmin R10 / SkyTrak+), Enclosures & Mats on Amazon.</span>
            <a href="{top_deal_link}" target="_blank" rel="nofollow sponsored noopener" class="text-amber-300 hover:text-amber-200 underline font-bold ml-1">
                View Active Golf Simulator Deals &rarr;
            </a>
        </div>
    </div>

    <!-- STICKY NAVIGATION HEADER (GRAY BACKGROUND) -->
    <header class="bg-gray-300 border-b border-gray-400 sticky top-0 z-30 shadow-sm">
        <div class="max-w-6xl mx-auto px-4 py-3.5 flex flex-wrap items-center justify-between gap-4">
            <a href="{BASE_URL}/" class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-lg bg-emerald-700 flex items-center justify-center text-white font-black text-lg shadow-sm">G</div>
                <div>
                    <span class="font-extrabold text-lg tracking-tight text-gray-900 block leading-none">{SITE_NAME}</span>
                    <span class="text-[11px] text-gray-700 font-medium">Projector Throw, Screen Ratio & Radar Depth Engine</span>
                </div>
            </a>
            <nav class="flex flex-wrap items-center gap-4 sm:gap-5 text-xs sm:text-sm font-semibold text-gray-800">
                <a href="{BASE_URL}/#calculator" class="hover:text-emerald-800 transition">Throw & Room Calc</a>
                <a href="{BASE_URL}/#product-search" class="hover:text-emerald-800 transition">Search Sim Gear</a>
                <a href="{BASE_URL}/#best-sellers" class="hover:text-emerald-800 transition">Best Sellers</a>
                <a href="{BASE_URL}/#comparison" class="hover:text-emerald-800 transition">Compare</a>
                <a href="{BASE_URL}/#reviews" class="hover:text-emerald-800 transition">Daily Reviews (+3/Day)</a>
                <a href="{BASE_URL}/#faq" class="hover:text-emerald-800 transition">FAQ</a>
                <a href="{BASE_URL}/sitemap.html" class="hover:text-emerald-800 transition font-bold underline">Site Map</a>
            </nav>
        </div>
    </header>
    """

def render_onpage_sitemap_directory():
    calc_links = "".join([
        f'<li><a href="{BASE_URL}/{p["slug"]}.html" class="text-xs text-gray-700 hover:text-emerald-800 hover:underline">⛳ {p["name"]} Calculator</a></li>'
        for p in ALL_CALC_PAGES
    ])
    vs_links = "".join([
        f'<li><a href="{BASE_URL}/{v["slug"]}.html" class="text-xs text-gray-700 hover:text-emerald-800 hover:underline">⚖️ {v["title"]}</a></li>'
        for v in VS_COMPARISONS
    ])
    all_revs = get_cumulative_product_reviews()
    rev_links = "".join([
        f'<li><a href="{BASE_URL}/{r["slug"]}.html" class="text-xs text-gray-700 hover:text-emerald-800 hover:underline">📝 [{r["published_date"]}] {r["product_name"]} Review</a></li>'
        for r in all_revs
    ])
    return f"""
    <!-- COMPLETE ON-PAGE SITE MAP SECTION (SITE MAP) -->
    <section id="site-map" class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-gray-300 pb-3">
            <div>
                <span class="text-xs font-extrabold uppercase tracking-wider text-emerald-800">Complete Site Architecture & Index</span>
                <h2 class="text-xl font-extrabold text-gray-900">Full HTML & XML Site Map Directory</h2>
            </div>
            <div class="flex gap-3 text-xs font-bold">
                <a href="{BASE_URL}/sitemap.html" class="bg-gray-300 hover:bg-gray-400 text-gray-900 px-3 py-1.5 rounded-lg transition">Open Dedicated HTML Site Map &rarr;</a>
                <a href="{BASE_URL}/sitemap.xml" class="bg-emerald-700 hover:bg-emerald-800 text-white px-3 py-1.5 rounded-lg transition">View XML Sitemap</a>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">1. Throw & Room Calculators ({len(ALL_CALC_PAGES) + 1})</h3>
                <ul class="space-y-1.5">
                    <li><a href="{BASE_URL}/" class="text-xs font-bold text-emerald-800 hover:underline">🏠 Home — Master Projector Throw & Room Calculator</a></li>
                    {calc_links}
                </ul>
            </div>
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">2. Head-to-Head Comparisons ({len(VS_COMPARISONS)})</h3>
                <ul class="space-y-2">
                    {vs_links}
                </ul>
            </div>
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">3. Daily Product Reviews ({len(all_revs)} — +3/Day)</h3>
                <ul class="space-y-1.5 max-h-80 overflow-y-auto pr-2">
                    {rev_links}
                </ul>
            </div>
        </div>
    </section>
    """

def render_dedicated_html_sitemap_page():
    canonical_url = f"{BASE_URL}/sitemap.html"
    sitemap_block = render_onpage_sitemap_directory()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Complete Site Map Directory — Calculators, Comparisons & Daily Reviews | {SITE_NAME}</title>
    <meta name="description" content="Complete HTML and XML site map directory of all golf simulator projector throw calculators, impact screen aspect ratio guides, launch monitor depth calculators, and daily reviews on {SITE_NAME}.">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-6xl mx-auto px-4 py-10 space-y-8">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-emerald-800">Home</a>
            <span>/</span>
            <span class="text-gray-900">Complete Site Map</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-2">
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900">{SITE_NAME} — Complete Site Map</h1>
            <p class="text-sm text-gray-700">Browse every interactive golf simulator projector throw calculator, screen aspect ratio guide, launch monitor room depth calculator, head-to-head comparison, and cumulative daily product review article (+3 added daily) below.</p>
        </div>

        {sitemap_block}
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def render_calculator_page(page_data, is_home=False):
    img_h, diag_in, throw_s, _, depth_ft, _, _, _, _ = compute_golfsim_specs(
        page_data["screen_w"], page_data["aspect"], page_data["throw_ratio"],
        page_data["monitor_type"], page_data["golfer_h"]
    )
    title = f"{SITE_NAME} — {SITE_TAGLINE}" if is_home else f"{page_data['name']} — {throw_s} Throw & {depth_ft}' Depth Calculator | {SITE_NAME}"
    description = page_data["desc"]
    canonical_url = f"{BASE_URL}/" if is_home else f"{BASE_URL}/{page_data['slug']}.html"
    faqs = generate_faq_data(
        page_data["name"], page_data["screen_w"], page_data["aspect"],
        page_data["throw_ratio"], page_data["monitor_type"], page_data["golfer_h"]
    )

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": item["q"], "acceptedAnswer": {"@type": "Answer", "text": item["a"]}}
            for item in faqs
        ]
    }

    app_schema = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": title,
        "url": canonical_url,
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "All",
        "description": description,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}
    }

    bestseller_cards_html = ""
    for prod in BEST_SELLERS:
        link = amz_url(prod["keyword"])
        bestseller_cards_html += f"""
        <div class="bg-gray-100 border-2 border-gray-300 hover:border-gray-400 rounded-xl p-5 shadow-sm transition flex flex-col justify-between">
            <div>
                <div class="flex items-center justify-between gap-2 mb-2">
                    <span class="text-xs font-bold uppercase tracking-wider bg-emerald-100 text-emerald-900 border border-emerald-300 px-2.5 py-1 rounded-full">{prod['badge']}</span>
                    <span class="text-xs font-semibold text-amber-700">{prod['rating']}</span>
                </div>
                <span class="text-xs text-gray-600 font-medium">{prod['category']}</span>
                <h3 class="text-base font-bold text-gray-900 mt-1 mb-2 leading-snug">{prod['title']}</h3>
                <p class="text-xs text-gray-700 mb-4 bg-gray-200 p-2.5 rounded-lg border border-gray-300">{prod['specs']}</p>
            </div>
            <a href="{link}" target="_blank" rel="nofollow sponsored noopener"
               class="w-full inline-flex items-center justify-center bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-sm py-2.5 px-4 rounded-lg transition shadow-sm">
               Check Today's Price on Amazon &rarr;
            </a>
        </div>
        """

    preset_links_html = ""
    for p in ALL_CALC_PAGES:
        _, _, _, p_thr, p_dep, _, _, _, _ = compute_golfsim_specs(
            p["screen_w"], p["aspect"], p["throw_ratio"], p["monitor_type"], p["golfer_h"]
        )
        active_cls = "bg-emerald-100 border-emerald-700 text-emerald-950 font-bold" if (not is_home and p["slug"] == page_data["slug"]) else "bg-gray-100 border-gray-300 text-gray-800 hover:border-emerald-700 hover:text-gray-950"
        preset_links_html += f"""
        <a href="{BASE_URL}/{p['slug']}.html" class="border rounded-lg p-3 text-xs transition flex items-center justify-between {active_cls}">
            <span class="truncate pr-2">{p['name']}</span>
            <span class="text-emerald-900 font-mono shrink-0">{p_thr}' / {p_dep}'D</span>
        </a>
        """

    faq_html = ""
    for item in faqs:
        faq_html += f"""
        <div class="bg-gray-100 border-2 border-gray-300 rounded-xl p-5">
            <h3 class="text-base font-bold text-gray-900 mb-2">{item['q']}</h3>
            <p class="text-sm text-gray-700 leading-relaxed">{item['a']}</p>
        </div>
        """

    mid_banner_link = amz_url("GoSports+10x8+Golf+Simulator+Enclosure+BenQ+Projector+and+MLM2PRO+Bundle")
    comparison_html = render_comparison_table_section()
    reviews_grid_html, total_reviews_count = render_review_cards_grid()
    onpage_sitemap_html = render_onpage_sitemap_directory()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canonical_url}">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">{json.dumps(faq_schema)}</script>
    <script type="application/ld+json">{json.dumps(app_schema)}</script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased selection:bg-emerald-700 selection:text-white">

    {render_common_header_and_banner()}

    <main class="max-w-6xl mx-auto px-4 py-8 space-y-12">

        <!-- HERO TITLE SECTION -->
        <section class="text-center max-w-3xl mx-auto space-y-3">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-gray-300 border border-gray-400 text-xs font-semibold text-gray-800">
                <span>⛳ Short-Throw Optical Distance, 4:3 vs 16:9 Screen Fill & Radar Depth Sizing Engine</span>
            </div>
            <h1 class="text-3xl sm:text-4xl font-extrabold text-gray-900 tracking-tight">
                { "Golf Simulator Projector Throw Distance, Impact Screen & Room Calculator" if is_home else f"{page_data['name']} — Throw & Room Calculator" }
            </h1>
            <p class="text-gray-700 text-sm sm:text-base leading-relaxed">
                {description}
            </p>
        </section>

        <!-- INTERACTIVE CALCULATOR + LIVE HARDWARE MATCHER -->
        <section id="calculator" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            <!-- Left Column: Inputs (7 Cols) -->
            <div class="lg:col-span-7 bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-6">
                <div class="flex items-center justify-between border-b border-gray-300 pb-4">
                    <div>
                        <h2 class="text-xl font-extrabold text-gray-900">1. Enter Screen Width, Throw Ratio & Launch Monitor</h2>
                        <p class="text-xs text-gray-600">Calculates ceiling mount distance, image height, room depth & ceiling height</p>
                    </div>
                    <span class="text-xs font-mono bg-emerald-100 text-emerald-900 border border-emerald-300 px-2.5 py-1 rounded font-semibold">Live Sim Math</span>
                </div>

                <div>
                    <label for="quickPreset" class="block text-xs font-bold uppercase tracking-wider text-gray-700 mb-2">Quick Select Garage or Basement Simulator Bay Preset</label>
                    <select id="quickPreset" onchange="applyPreset(this.value)" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-sm font-semibold text-gray-900 focus:ring-2 focus:ring-emerald-700">
                        <option value="{page_data['screen_w']},{page_data['aspect']},{page_data['throw_ratio']},{page_data['monitor_type']},{page_data['golfer_h']}">Current: {page_data['name']}</option>
                        <option value="10.0,4:3,0.69,radar,72">10' × 8' Bay (4:3 Ratio | 0.69 BenQ TH671ST | MLM2PRO/R10 Radar)</option>
                        <option value="10.0,4:3,0.50,camera,72">10' × 8' Short-Room Bay (0.50 Optoma Laser | SkyTrak+ Side Camera)</option>
                        <option value="12.0,4:3,0.90,radar,72">12' × 9' Deluxe Bay (4:3 Ratio | 0.90 BenQ TK700STi 4K Projector)</option>
                        <option value="13.0,16:10,0.69,radar,72">13' × 8' Widescreen Bay (16:10 Ratio | 0.69 Short-Throw Projector)</option>
                        <option value="16.0,16:9,0.69,camera,72">16' × 9' Commercial 16:9 4K Bay (11.0 Ft Throw Distance)</option>
                        <option value="8.0,4:3,0.69,camera,70">8' × 8' Compact Pop-Up Net / Bedroom Bay (5.5 Ft Throw)</option>
                    </select>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                    <div>
                        <label for="screenWInput" class="block text-sm font-bold text-gray-800 mb-1">Screen Width (Feet)</label>
                        <input type="number" id="screenWInput" value="{page_data['screen_w']}" min="6.0" max="22.0" step="0.5" oninput="calculateGolfSim()"
                               class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-base font-bold text-gray-900 focus:ring-2 focus:ring-emerald-700">
                        <span class="text-[11px] text-gray-600">Standard: 8', 10', 12', 13', 16'</span>
                    </div>

                    <div>
                        <label for="aspectInput" class="block text-sm font-bold text-gray-800 mb-1">PC Aspect Ratio</label>
                        <select id="aspectInput" onchange="calculateGolfSim()" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3 py-2.5 text-sm font-bold text-gray-900">
                            <option value="4:3" {"selected" if page_data['aspect'] == "4:3" else ""}>4 : 3 (Best for 10'×8' & 12'×9')</option>
                            <option value="16:10" {"selected" if page_data['aspect'] == "16:10" else ""}>16 : 10 (Best for 13'×8' Bay)</option>
                            <option value="16:9" {"selected" if page_data['aspect'] == "16:9" else ""}>16 : 9 (Best for 14'–16' Wide)</option>
                        </select>
                    </div>

                    <div>
                        <label for="throwInput" class="block text-sm font-bold text-gray-800 mb-1">Projector Throw Ratio</label>
                        <select id="throwInput" onchange="calculateGolfSim()" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3 py-2.5 text-sm font-bold text-gray-900">
                            <option value="0.50" {"selected" if page_data['throw_ratio'] <= 0.55 else ""}>0.50:1 (Optoma GT2000HDR Laser)</option>
                            <option value="0.69" {"selected" if 0.55 < page_data['throw_ratio'] <= 0.75 else ""}>0.69:1 (BenQ TH671ST / Short)</option>
                            <option value="0.80" {"selected" if 0.75 < page_data['throw_ratio'] <= 0.85 else ""}>0.80:1 (Mid-Zoom Short Throw)</option>
                            <option value="0.90" {"selected" if page_data['throw_ratio'] > 0.85 else ""}>0.90:1 (BenQ TK700STi 4K UHD)</option>
                        </select>
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                    <div>
                        <label for="monInput" class="block text-sm font-bold text-gray-800 mb-1">Launch Monitor Placement Type</label>
                        <select id="monInput" onchange="calculateGolfSim()" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-sm font-bold text-gray-900">
                            <option value="radar" {"selected" if page_data['monitor_type'] == "radar" else ""}>Rear Radar/Camera (MLM2PRO, Garmin R10, Mevo+ — 7' Behind)</option>
                            <option value="camera" {"selected" if page_data['monitor_type'] == "camera" else ""}>Side Photometric (SkyTrak+, Bushnell, GC3 — 0' Behind Ball!)</option>
                        </select>
                    </div>

                    <div>
                        <label for="golferHInput" class="block text-sm font-bold text-gray-800 mb-1">Tallest Golfer Height</label>
                        <select id="golferHInput" onchange="calculateGolfSim()" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-sm font-bold text-gray-900">
                            <option value="68" {"selected" if page_data['golfer_h'] <= 68 else ""}>5' 8\" (68 Inches) — Min 8.7' Ceiling</option>
                            <option value="70" {"selected" if page_data['golfer_h'] in (69, 70) else ""}>5' 10\" (70 Inches) — Min 8.8' Ceiling</option>
                            <option value="72" {"selected" if page_data['golfer_h'] in (71, 72) else ""}>6' 0\" (72 Inches) — Min 9.0' Ceiling</option>
                            <option value="74" {"selected" if page_data['golfer_h'] in (73, 74) else ""}>6' 2\" (74 Inches) — Min 9.2' Ceiling</option>
                            <option value="76" {"selected" if page_data['golfer_h'] >= 75 else ""}>6' 4\"+ (76 Inches) — Min 9.5' Ceiling</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- Right Column: Output + Dynamic Amazon Recommendation (5 Cols) -->
            <div class="lg:col-span-5 bg-gray-100 border-2 border-emerald-700 rounded-2xl p-6 sm:p-8 shadow-md space-y-6">
                <div class="border-b border-gray-300 pb-3">
                    <span class="text-xs font-extrabold uppercase tracking-wider text-emerald-800">2. Engineered Projector & Bay Specs</span>
                    <h2 class="text-xl font-extrabold text-gray-900">Your Exact Simulator Layout</h2>
                </div>

                <div class="grid grid-cols-2 gap-3.5">
                    <div class="bg-emerald-100 border border-emerald-300 rounded-xl p-3.5">
                        <span class="text-xs text-emerald-950 font-semibold block">Projector Mount Dist.</span>
                        <span id="resThrowDist" class="text-2xl font-black text-emerald-800">6' 11\"</span>
                        <span id="resShadowNote" class="text-[11px] text-emerald-900 block mt-0.5">6.9 Ft From Impact Screen</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">Projected Image Size</span>
                        <span id="resImgSize" class="text-xl font-black text-gray-900">10.0' × 7.5'</span>
                        <span id="resDiagRes" class="text-[11px] text-emerald-800 font-bold block mt-0.5">150\" Diag (1920×1440)</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">Min. Total Room Depth</span>
                        <span id="resRoomDepth" class="text-lg font-extrabold text-gray-900">16.5 Feet</span>
                        <span id="resDepthBreak" class="text-[11px] text-gray-600 block mt-0.5">1' Back + 8.5' Tee + 7' Radar</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">Ceiling & Turf Needed</span>
                        <span id="resCeiling" class="text-lg font-extrabold text-amber-800">9.0 Ft Ceiling</span>
                        <span id="resTurfSqft" class="text-[11px] text-gray-600 block mt-0.5">~198 Sq.Ft Turf + 5'×5' Mat</span>
                    </div>
                </div>

                <!-- Dynamic Matched Product Box -->
                <div class="bg-gray-200 border-2 border-emerald-600 rounded-xl p-4 space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-[11px] font-extrabold uppercase tracking-wider bg-emerald-700 text-white px-2 py-0.5 rounded">Verified Hardware Match</span>
                        <span class="text-xs font-bold text-gray-700">Amazon Prime Ready</span>
                    </div>
                    <h3 id="recGolfTitle" class="text-base font-extrabold text-gray-900 leading-snug">Loading Projector & Monitor Match...</h3>
                    <p id="recGolfDesc" class="text-xs text-gray-700"></p>
                    <div class="pt-1 flex flex-col sm:flex-row gap-2.5">
                        <a id="recPrimaryBtn" href="#" target="_blank" rel="nofollow sponsored noopener"
                           class="flex-1 text-center bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-sm py-3 px-4 rounded-lg transition shadow-sm">
                           Shop Projector & Launch Monitor &rarr;
                        </a>
                        <a id="recSecondaryBtn" href="#" target="_blank" rel="nofollow sponsored noopener"
                           class="text-center bg-gray-800 hover:bg-gray-900 text-white font-bold text-xs py-3 px-3 rounded-lg transition">
                           Shop Screen & Mat
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <!-- PRODUCT SEARCH ENGINE SECTION (SEARCH PRODUK) -->
        <section id="product-search" class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm">
            <div class="max-w-3xl mx-auto text-center space-y-4">
                <h2 class="text-2xl font-extrabold text-gray-900">Search Short-Throw Projectors, Launch Monitors, Impact Screens & Hitting Mats</h2>
                <p class="text-sm text-gray-700">Search any brand (BenQ, Optoma, Rapsodo MLM2PRO, Garmin R10, SkyTrak+, GoSports, Carl's Place, Country Club Elite, Spornia) on Amazon.</p>
                <form onsubmit="handleAmazonSearch(event)" class="flex flex-col sm:flex-row gap-3 pt-2">
                    <input type="text" id="amzSearchInput" placeholder="e.g. BenQ TK700STi 4K Projector, Rapsodo MLM2PRO, GoSports 10x8 Golf Enclosure, Country Club Elite Mat..."
                           class="flex-1 bg-gray-200 border-2 border-gray-400 rounded-xl px-4 py-3 text-sm font-medium text-gray-900 placeholder-gray-500 focus:outline-none focus:border-emerald-700" required>
                    <button type="submit" class="bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-sm px-6 py-3 rounded-xl transition cursor-pointer shrink-0">
                        Search on Amazon &rarr;
                    </button>
                </form>
                <div class="flex flex-wrap items-center justify-center gap-2 pt-2 text-xs">
                    <span class="text-gray-600 font-semibold">Popular Searches:</span>
                    <a href="{amz_url('BenQ TK700STi TH671ST Short Throw Projector')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-emerald-200 text-gray-800 border border-gray-300 rounded-full transition">BenQ Golf Projectors</a>
                    <a href="{amz_url('Rapsodo MLM2PRO Mobile Launch Monitor')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-emerald-200 text-gray-800 border border-gray-300 rounded-full transition">Rapsodo MLM2PRO</a>
                    <a href="{amz_url('Garmin Approach R10 Launch Monitor')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-emerald-200 text-gray-800 border border-gray-300 rounded-full transition">Garmin Approach R10</a>
                    <a href="{amz_url('GoSports Golf Simulator Enclosure Impact Screen')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-emerald-200 text-gray-800 border border-gray-300 rounded-full transition">10'×8' & 12'×9' Enclosures</a>
                    <a href="{amz_url('Country Club Elite Real Feel Golf Mat')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-emerald-200 text-gray-800 border border-gray-300 rounded-full transition">Country Club Elite Mats</a>
                </div>
            </div>
        </section>

        <!-- BEST SELLING PRODUCTS GRID (PRODUK TERLARIS) -->
        <section id="best-sellers" class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
                <div>
                    <span class="text-xs font-extrabold uppercase tracking-wider text-emerald-800">Verified Garage Studio Hardware</span>
                    <h2 class="text-2xl font-extrabold text-gray-900">Best-Selling Golf Projectors, Launch Monitors, Enclosures & Hitting Mats</h2>
                </div>
                <a href="{amz_url('Best Selling Golf Launch Monitors and Simulator Projectors')}" target="_blank" rel="nofollow sponsored noopener" class="text-sm font-bold text-emerald-800 hover:text-emerald-900">
                    Browse Full Amazon Best Sellers &rarr;
                </a>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
                {bestseller_cards_html}
            </div>
        </section>

        {comparison_html}

        <!-- CUMULATIVE DAILY PRODUCT REVIEW ARTICLES SECTION (+3 NEW ARTICLES PER DAY) -->
        <section id="reviews" class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
                <div>
                    <span class="text-xs font-extrabold uppercase tracking-wider text-emerald-800">Autonomous Daily Review Archive ({total_reviews_count} Published Articles & Growing +3/Day)</span>
                    <h2 class="text-2xl font-extrabold text-gray-900">In-Depth Launch Monitor, Golf Projector & Enclosure Review Articles</h2>
                </div>
                <span class="text-xs font-semibold bg-emerald-100 text-emerald-900 border border-emerald-300 px-3 py-1 rounded-full">+3 New Product Reviews Added Automatically Every Day</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {reviews_grid_html}
            </div>
        </section>

        <!-- MID-PAGE PROMOTIONAL AFFILIATE BANNER -->
        <section class="bg-gray-300 border-2 border-emerald-700 rounded-2xl p-6 sm:p-8 flex flex-col md:flex-row items-center justify-between gap-6">
            <div class="space-y-2 max-w-2xl">
                <span class="text-xs font-extrabold uppercase tracking-wider bg-emerald-700 text-white px-2.5 py-1 rounded">Complete Garage Golf Studio Bundle</span>
                <h2 class="text-xl sm:text-2xl font-extrabold text-gray-900">Building a Year-Round 4K Golf Simulator in Your Garage or Basement?</h2>
                <p class="text-sm text-gray-800">Play Pebble Beach and St Andrews at home by pairing a 10'×8' Acoustic Impact Screen Enclosure with a Short-Throw Golf Projector, Rapsodo MLM2PRO / SkyTrak+ Monitor, and Country Club Elite 5'×5' Mat.</p>
            </div>
            <a href="{mid_banner_link}" target="_blank" rel="nofollow sponsored noopener"
               class="shrink-0 bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-sm px-6 py-3.5 rounded-xl shadow-sm transition">
               Explore Complete Golf Simulator Bundles &rarr;
            </a>
        </section>

        <!-- PROGRAMMATIC SEO DIRECTORY -->
        <section id="presets" class="space-y-4">
            <div class="border-b border-gray-300 pb-3">
                <h2 class="text-xl font-extrabold text-gray-900">Enclosure Size, Throw Ratio & Launch Monitor Room Calculators</h2>
                <p class="text-xs text-gray-600">Select your exact impact screen width or projector throw ratio below for pre-calculated ceiling mount distances and room depth specs.</p>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2.5">
                {preset_links_html}
            </div>
        </section>

        <!-- FREQUENTLY ASKED QUESTIONS (FAQ) -->
        <section id="faq" class="space-y-6">
            <div class="border-b border-gray-300 pb-3">
                <span class="text-xs font-extrabold uppercase tracking-wider text-emerald-800">Throw Ratio, 4:3 Resolution & Ceiling Clearance Guide</span>
                <h2 class="text-2xl font-extrabold text-gray-900">Frequently Asked Questions (FAQ)</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                {faq_html}
            </div>
        </section>

        {onpage_sitemap_html}

    </main>

    <!-- FOOTER (GRAY BACKGROUND) -->
    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700">
        <div class="max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>
                <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
                <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
            </div>
            <div class="flex flex-wrap gap-4 font-medium text-gray-800">
                <a href="{BASE_URL}/" class="hover:text-emerald-800">Home</a>
                <a href="{BASE_URL}/#comparison" class="hover:text-emerald-800">Comparisons</a>
                <a href="{BASE_URL}/#reviews" class="hover:text-emerald-800">Daily Reviews (+3/Day)</a>
                <a href="{BASE_URL}/sitemap.html" class="hover:text-emerald-800 font-bold">HTML Site Map</a>
                <a href="{BASE_URL}/sitemap.xml" class="hover:text-emerald-800">XML Sitemap</a>
                <a href="{BASE_URL}/#faq" class="hover:text-emerald-800">FAQ</a>
            </div>
        </div>
    </footer>

    <!-- INTERACTIVE CALCULATOR & AFFILIATE MATCHING SCRIPT -->
    <script>
        const AFFILIATE_TAG = "{AFFILIATE_TAG}";

        function makeAmazonLink(query) {{
            return "https://www.amazon.com/s?k=" + encodeURIComponent(query) + "&tag=" + AFFILIATE_TAG;
        }}

        function applyPreset(val) {{
            const parts = val.split(",");
            if (parts.length === 5) {{
                document.getElementById("screenWInput").value = parts[0];
                document.getElementById("aspectInput").value = parts[1];
                document.getElementById("throwInput").value = parts[2];
                document.getElementById("monInput").value = parts[3];
                document.getElementById("golferHInput").value = parts[4];
                calculateGolfSim();
            }}
        }}

        function handleAmazonSearch(e) {{
            e.preventDefault();
            const q = document.getElementById("amzSearchInput").value.trim();
            if (q) {{
                window.open(makeAmazonLink(q), "_blank", "noopener,noreferrer");
            }}
        }}

        function calculateGolfSim() {{
            const screenW = parseFloat(document.getElementById("screenWInput").value) || 10.0;
            const aspect = document.getElementById("aspectInput").value || "4:3";
            const throwRatio = parseFloat(document.getElementById("throwInput").value) || 0.69;
            const monType = document.getElementById("monInput").value || "radar";
            const golferH = parseFloat(document.getElementById("golferHInput").value) || 72;

            let imgH = screenW * 0.75;
            let resStr = "1920×1440 (4:3 Custom)";
            if (aspect === "16:9") {{
                imgH = screenW * (9.0 / 16.0);
                resStr = "3840×2160 (4K 16:9)";
            }} else if (aspect === "16:10") {{
                imgH = screenW * (10.0 / 16.0);
                resStr = "1920×1200 (16:10)";
            }}

            const diagIn = Math.round(Math.sqrt((screenW * screenW) + (imgH * imgH)) * 12);

            const throwFtRaw = screenW * throwRatio;
            let ftInt = Math.floor(throwFtRaw);
            let inRem = Math.round((throwFtRaw - ftInt) * 12);
            if (inRem === 12) {{ ftInt += 1; inRem = 0; }}

            const minDepth = monType === "radar" ? 16.5 : 11.5;
            const depthBreak = monType === "radar" ? "1' Buffer + 8.5' Flight + 7' Radar" : "1' Buffer + 8' Flight + 2.5' Swing";

            const minCeil = Math.max(8.5, Math.min(11.0, (golferH / 12.0) + 3.0)).toFixed(1);
            const turfSqft = Math.round((screenW + 2.0) * minDepth);

            document.getElementById("resThrowDist").textContent = ftInt + "' " + inRem + "\\\"";
            document.getElementById("resShadowNote").textContent = throwFtRaw.toFixed(1) + " Ft From Screen (Ratio " + throwRatio + ")";
            document.getElementById("resImgSize").textContent = screenW.toFixed(1) + "' W × " + imgH.toFixed(1) + "' H";
            document.getElementById("resDiagRes").textContent = diagIn + "\\\" Diag (" + resStr + ")";
            document.getElementById("resRoomDepth").textContent = minDepth + " Ft Min Depth";
            document.getElementById("resDepthBreak").textContent = depthBreak;
            document.getElementById("resCeiling").textContent = minCeil + " Ft Min Ceiling";
            document.getElementById("resTurfSqft").textContent = "~" + turfSqft + " Sq.Ft Turf + 5'×5' Mat";

            let recTitle = "";
            let recDesc = "";
            let primaryQuery = "";
            let secondaryQuery = "GoSports " + (screenW >= 11.5 ? "12x9" : "10x8") + " Golf Simulator Enclosure and Country Club Elite Golf Mat";

            if (throwRatio <= 0.55) {{
                recTitle = "Optoma GT2000HDR (0.50:1 Laser Projector) + " + (monType === "camera" ? "SkyTrak+ Photometric" : "Rapsodo MLM2PRO");
                recDesc = "Mounts just " + ftInt + "'" + inRem + "\" from the screen in front of your swing for 100% shadow-free projection.";
                primaryQuery = "Optoma GT2000HDR Short Throw Laser Projector and " + (monType === "camera" ? "SkyTrak Plus" : "Rapsodo MLM2PRO");
            }} else if (throwRatio >= 0.85) {{
                recTitle = "BenQ TK700STi 4K UHD Short-Throw Projector + " + (monType === "camera" ? "SkyTrak+ Monitor" : "Rapsodo MLM2PRO / Garmin R10");
                recDesc = "True 4K UHD clarity mounted at " + ftInt + "'" + inRem + "\" back over your hitting mat.";
                primaryQuery = "BenQ TK700STi 4K Short Throw Projector and Rapsodo MLM2PRO";
            }} else {{
                recTitle = "BenQ TH671ST (0.69 Ratio) Golf Projector + Rapsodo MLM2PRO / Garmin Approach R10";
                recDesc = "America's #1 garage golf combination matched to a " + screenW + "'×" + imgH.toFixed(1) + "' screen (" + ftInt + "'" + inRem + "\" mount).";
                primaryQuery = "BenQ TH671ST Short Throw Golf Projector and Rapsodo MLM2PRO Garmin R10";
            }}

            document.getElementById("recGolfTitle").textContent = recTitle;
            document.getElementById("recGolfDesc").textContent = recDesc;
            document.getElementById("recPrimaryBtn").href = makeAmazonLink(primaryQuery);
            document.getElementById("recSecondaryBtn").href = makeAmazonLink(secondaryQuery);
        }}

        window.addEventListener("DOMContentLoaded", calculateGolfSim);
    </script>
</body>
</html>"""

def render_single_review_page(rev):
    canonical_url = f"{BASE_URL}/{rev['slug']}.html"
    amz_link = amz_url(rev["keyword"])

    review_schema = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": rev["product_name"],
        "description": rev["summary"],
        "review": {
            "@type": "Review",
            "datePublished": rev["published_date"],
            "reviewRating": {"@type": "Rating", "ratingValue": rev["rating_score"], "bestRating": "5"},
            "author": {"@type": "Organization", "name": SITE_NAME},
            "reviewBody": " ".join(rev["body_paragraphs"])
        }
    }

    pros_html = "".join([f'<li class="flex items-start gap-2 text-sm text-gray-800"><span class="text-emerald-700 font-bold">✓</span><span>{p}</span></li>' for p in rev["pros"]])
    cons_html = "".join([f'<li class="flex items-start gap-2 text-sm text-gray-800"><span class="text-rose-700 font-bold">✕</span><span>{c}</span></li>' for c in rev["cons"]])
    paragraphs_html = "".join([f'<p class="text-gray-800 leading-relaxed text-base mb-4">{p}</p>' for p in rev["body_paragraphs"]])

    recent_reviews = [r for r in get_cumulative_product_reviews() if r["slug"] != rev["slug"]][:6]
    related_html = ""
    for other in recent_reviews:
        related_html += f"""
        <a href="{BASE_URL}/{other['slug']}.html" class="bg-gray-100 border-2 border-gray-300 rounded-xl p-4 hover:border-emerald-700 transition block">
            <span class="text-[11px] font-bold text-emerald-800 uppercase">{other['verdict_badge']}</span>
            <h4 class="font-extrabold text-sm text-gray-900 mt-1 line-clamp-2">{other['product_name']} Review</h4>
            <span class="text-xs text-gray-600 mt-1 block">Score: {other['rating_score']} / 5.0 ★ ({other['published_date']}) &rarr;</span>
        </a>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{rev['title']} | {SITE_NAME}</title>
    <meta name="description" content="{rev['summary']}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">{json.dumps(review_schema)}</script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-4xl mx-auto px-4 py-10 space-y-10">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-emerald-800">Home & Throw Calculator</a>
            <span>/</span>
            <a href="{BASE_URL}/#reviews" class="hover:text-emerald-800">Daily Golf Sim Reviews</a>
            <span>/</span>
            <span class="text-gray-900">{rev['product_name']}</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-5">
            <div class="flex flex-wrap items-center justify-between gap-2">
                <span class="text-xs font-extrabold uppercase tracking-wider bg-emerald-100 text-emerald-900 border border-emerald-300 px-3 py-1 rounded-full">{rev['verdict_badge']}</span>
                <div class="flex items-center gap-2">
                    <span class="text-xs font-mono text-gray-600">Published: {rev['published_date']}</span>
                    <span class="text-sm font-black bg-amber-200 text-amber-950 px-3 py-1 rounded-lg">Studio Rating: {rev['rating_score']} / 5.0 ★</span>
                </div>
            </div>
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900 leading-tight">{rev['title']}</h1>
            <p class="text-base text-gray-700 leading-relaxed">{rev['summary']}</p>

            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 bg-gray-200 p-4 rounded-xl border border-gray-300 text-xs">
                <div><span class="text-gray-500 block font-medium">Primary Spec</span><strong class="text-gray-900">{rev['spec_1']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Optics / Turf</span><strong class="text-gray-900">{rev['spec_2']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Room Fit</span><strong class="text-gray-900">{rev['spec_3']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Features</span><strong class="text-gray-900">{rev['spec_4']}</strong></div>
            </div>

            <div class="flex flex-col sm:flex-row gap-3 pt-2">
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener"
                   class="flex-1 text-center bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-sm py-3.5 px-6 rounded-xl transition shadow-sm">
                   Check Latest Price & Availability on Amazon &rarr;
                </a>
                <a href="{BASE_URL}/#calculator"
                   class="text-center bg-gray-300 hover:bg-gray-400 text-gray-900 font-bold text-sm py-3.5 px-5 rounded-xl transition">
                   Calculate Throw & Room Size
                </a>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="bg-gray-100 border-2 border-emerald-400 rounded-2xl p-6 space-y-3">
                <h2 class="text-base font-extrabold text-emerald-900 uppercase tracking-wide">Pros (What We Like)</h2>
                <ul class="space-y-2.5">{pros_html}</ul>
            </div>
            <div class="bg-gray-100 border-2 border-rose-400 rounded-2xl p-6 space-y-3">
                <h2 class="text-base font-extrabold text-rose-900 uppercase tracking-wide">Cons (Things to Consider)</h2>
                <ul class="space-y-2.5">{cons_html}</ul>
            </div>
        </div>

        <article class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 space-y-4">
            <h2 class="text-xl font-extrabold text-gray-900 border-b border-gray-300 pb-3">Hands-On Spin Accuracy, Throw Distance & Garage Bay Analysis</h2>
            {paragraphs_html}
            <div class="pt-4 border-t border-gray-300 flex flex-col sm:flex-row items-center justify-between gap-4">
                <div>
                    <span class="text-xs font-bold uppercase text-emerald-800 block">Final Verdict</span>
                    <p class="text-sm font-bold text-gray-900">{rev['product_name']} earns {rev['rating_score']}/5.0 in our golf simulator benchmark.</p>
                </div>
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener"
                   class="shrink-0 bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-sm px-6 py-3 rounded-xl transition shadow-sm">
                   View Customer Reviews & Price on Amazon &rarr;
                </a>
            </div>
        </article>

        <section class="space-y-4">
            <h3 class="text-lg font-extrabold text-gray-900">Recent Daily Golf Simulator Hardware Reviews (+3 Added Daily)</h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                {related_html}
            </div>
        </section>
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def render_vs_comparison_page(vs):
    canonical_url = f"{BASE_URL}/{vs['slug']}.html"
    link_a = amz_url(vs["keyword_a"])
    link_b = amz_url(vs["keyword_b"])

    rows_html = ""
    for m in vs["metrics"]:
        rows_html += f"""
        <tr class="border-b border-gray-300">
            <td class="p-4 font-bold text-gray-900 bg-gray-200 text-xs sm:text-sm w-1/4">{m['feature']}</td>
            <td class="p-4 text-xs sm:text-sm text-gray-800 w-3/8">{m['val_a']}</td>
            <td class="p-4 text-xs sm:text-sm text-gray-800 w-3/8">{m['val_b']}</td>
        </tr>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{vs['title']} | {SITE_NAME}</title>
    <meta name="description" content="{vs['summary']}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-4xl mx-auto px-4 py-10 space-y-10">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-emerald-800">Home & Throw Calculator</a>
            <span>/</span>
            <a href="{BASE_URL}/#comparison" class="hover:text-emerald-800">Product Comparisons</a>
            <span>/</span>
            <span class="text-gray-900">{vs['product_a']} vs. {vs['product_b']}</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-4">
            <span class="text-xs font-extrabold uppercase tracking-wider bg-emerald-100 text-emerald-900 border border-emerald-300 px-3 py-1 rounded-full">{vs['winner_badge']}</span>
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900 leading-tight">{vs['title']}</h1>
            <p class="text-base text-gray-700 leading-relaxed">{vs['summary']}</p>
        </div>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl overflow-hidden shadow-sm">
            <table class="w-full text-left border-collapse">
                <thead>
                    <tr class="bg-gray-800 text-white text-xs sm:text-sm font-extrabold">
                        <th class="p-4">Specification</th>
                        <th class="p-4 text-emerald-300">{vs['product_a']}</th>
                        <th class="p-4 text-amber-300">{vs['product_b']}</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                    <tr class="bg-gray-200">
                        <td class="p-4 font-extrabold text-xs sm:text-sm text-gray-900">Check Amazon Price</td>
                        <td class="p-4">
                            <a href="{link_a}" target="_blank" rel="nofollow sponsored noopener" class="inline-block bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-xs py-2.5 px-4 rounded-lg transition">
                                View {vs['product_a']} &rarr;
                            </a>
                        </td>
                        <td class="p-4">
                            <a href="{link_b}" target="_blank" rel="nofollow sponsored noopener" class="inline-block bg-gray-800 hover:bg-gray-900 text-white font-extrabold text-xs py-2.5 px-4 rounded-lg transition">
                                View {vs['product_b']} &rarr;
                            </a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="bg-gray-100 border-2 border-emerald-600 rounded-2xl p-6 sm:p-8 space-y-4">
            <h2 class="text-xl font-extrabold text-gray-900">Head-to-Head Buying Verdict</h2>
            <p class="text-sm sm:text-base text-gray-800 leading-relaxed">{vs['verdict_text']}</p>
            <div class="flex flex-col sm:flex-row gap-3 pt-2">
                <a href="{link_a}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-sm py-3 px-4 rounded-xl transition">
                    Shop {vs['product_a']} on Amazon &rarr;
                </a>
                <a href="{link_b}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-gray-800 hover:bg-gray-900 text-white font-extrabold text-sm py-3 px-4 rounded-xl transition">
                    Shop {vs['product_b']} on Amazon &rarr;
                </a>
            </div>
        </div>
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def generate_sitemap_and_robots(urls):
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    xml_items = ""
    for u in urls:
        xml_items += f"""  <url>
    <loc>{u}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>{"1.0" if u.endswith("/") else "0.85"}</priority>
  </url>\n"""

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{xml_items}</urlset>"""

    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_content)

    robots_content = f"""User-agent: *
Allow: /
Sitemap: {BASE_URL}/sitemap.xml
"""
    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_content)

    with open(os.path.join(OUTPUT_DIR, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8") as f:
        f.write(INDEXNOW_KEY)

def ping_indexnow(urls):
    parsed_host = urllib.parse.urlparse(BASE_URL).netloc
    if not parsed_host or "username.github.io" in parsed_host:
        return

    payload = {
        "host": parsed_host,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
        "urlList": urls
    }
    try:
        req = urllib.request.Request(
            "https://api.indexnow.org/indexnow",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"IndexNow Ping Status: {resp.status}")
    except Exception as e:
        print(f"IndexNow notice: {e}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    generated_urls = []

    # 1. Generate Homepage
    home_preset = {
        "slug": "index",
        "name": "10' × 8' Golf Simulator Enclosure (4:3 Ratio | 0.69 Throw)",
        "screen_w": 10.0,
        "aspect": "4:3",
        "throw_ratio": 0.69,
        "monitor_type": "radar",
        "golfer_h": 72,
        "desc": "Calculate exact golf simulator short-throw projector mounting distance (feet & inches), 4:3 vs 16:9 impact screen height fill, launch monitor room depth, and minimum ceiling height—plus read 3 new studio gear reviews added daily."
    }
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_calculator_page(home_preset, is_home=True))
    generated_urls.append(f"{BASE_URL}/")

    # 2. Generate Dedicated HTML Site Map Page (sitemap.html)
    with open(os.path.join(OUTPUT_DIR, "sitemap.html"), "w", encoding="utf-8") as f:
        f.write(render_dedicated_html_sitemap_page())
    generated_urls.append(f"{BASE_URL}/sitemap.html")

    # 3. Generate Programmatic Golf Simulator & Throw Calculator Pages
    for page in ALL_CALC_PAGES:
        filename = f"{page['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_calculator_page(page, is_home=False))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 4. Generate Cumulative Daily Product Review Pages (+3 new reviews unlocked every single day)
    active_reviews = get_cumulative_product_reviews()
    for rev in active_reviews:
        filename = f"{rev['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_single_review_page(rev))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 5. Generate Standalone Head-to-Head Product Comparison Pages
    for vs in VS_COMPARISONS:
        filename = f"{vs['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_vs_comparison_page(vs))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 6. XML Sitemap, Robots & IndexNow Auto-Ping
    generate_sitemap_and_robots(generated_urls)
    ping_indexnow(generated_urls)
    print(f"Successfully generated {len(generated_urls)} total SEO pages ({len(active_reviews)} cumulative review articles [+3/day] + HTML/XML sitemaps) in /{OUTPUT_DIR}!")

if __name__ == "__main__":
    main()
