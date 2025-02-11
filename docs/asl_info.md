# American Sign Language (ASL)

## Linguistic Structure

### Core Components
- **Phonology**: Five parameters define each sign
  * Handshape: The configuration of the hand(s)
  * Palm orientation: Direction the palm faces
  * Location: Where the sign is made relative to the body
  * Movement: How the hands move during signing
  * Non-manual markers: Facial expressions and body movements

### Sign Types
1. **Free Morpheme Signs**
   * Basic, standalone signs
   * Cannot be broken down into smaller meaningful units
   * Example: "TREE", "HOUSE", "CAT"

2. **Compound Signs**
   * Combination of two or more signs
   * Example: "PARENT" (combination of "MOTHER" + "FATHER")
   * Often undergo movement reduction

3. **Fingerspelled Signs**
   * Represent English words letter by letter
   * Used for:
     - Proper names
     - Technical terms
     - Words without established signs
     - Emphasis or clarification

## Grammar and Syntax

### Sentence Structures
4. **Topic-Comment Structure**
   * Most common ASL pattern
   * Topic is signed first, followed by comment
   * Examples:
     - "MOVIE TOMORROW, I GO" (I'm going to the movie tomorrow)
     - "BOOK, I ALREADY READ" (I've already read the book)

>**Note:**
> No need for temporal synchronization with output of **NMS** since the sentence structure itself is different.

5. **Time-Topic-Comment**
   * Used for temporal references
   * Time element always comes first
   * Examples:
     - "LAST-WEEK, STORE, I GO" (I went to the store last week)
     - "FUTURE, HOUSE, I BUY" (I will buy a house)

### Question Formation
6. **Yes/No Questions**
   * Raised eyebrows
   * Slight forward head tilt
   * Body leans forward
   * Last sign often held longer

7. **Wh-Questions**
   * Question sign at end of sentence
   * Furrowed brows
   * Head slightly tilted
   * Common questions:
     - WHERE
     - WHAT
     - WHO
     - WHY
     - HOW
     - WHEN

>**Note:**
>Handling the questions would be very complicated especially for Yes/No questions since it involves other physical ques.
>Therefore we might want to use video features while audio correction as well.

## Speed and Timing

### Signing Speeds
8. **Conversational Rates**
   * Beginner: 30-60 signs per minute
   * Intermediate: 60-120 signs per minute
   * Advanced: 100-150 signs per minute
   * Native/Expert: 150-200+ signs per minute

9. **Duration Metrics**
   * Single sign: 400-600ms average
   * Compound signs: 600-800ms
   * Fingerspelled letters: 150-250ms each

10. **Context-Specific Speeds**
   * Educational setting: 50-100 signs per minute
   * Professional interpreting: 100-180 signs per minute
   * Casual conversation: 120-140 signs per minute
   * Story-telling: 80-120 signs per minute

### Fingerspelling Metrics
11. **Speed Categories**
   * Beginner: 1-2 letters per second
   * Intermediate: 2-3 letters per second
   * Advanced: 3-5 letters per second
   * Expert: 4-7 letters per second

12. **Word Length Impact**
   * Short words (1-3 letters): ~500ms total
   * Medium words (4-6 letters): ~1000ms total
   * Long words (7+ letters): ~1500-2000ms total

>**Note:**
>Each signs only takes ~500-1000 ms each on average. In 30 FPS video this amounts to roughly 15-30 frames. This is very small input. We might have to utilize higher FPS videos.

>**Todo:**
> Verify how long the signs take in training dataset.