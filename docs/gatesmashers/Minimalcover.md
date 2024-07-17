Step 1: Decompose the Functional Dependencies

The first step is to decompose the functional dependencies into single attribute dependencies if they are not already in that form.

Given functional dependencies:

1. \( A $\rightarrow $ B \)
2. \( C $\rightarrow $ B \)
3. \( D $\rightarrow $ ABC \)
4. \( AC $\rightarrow $ D )

### Step 2: Remove Extraneous Attributes

Next, we need to check for and remove any extraneous attributes from the left-hand side of the dependencies.

1. \( A $\rightarrow $ B \) (No extraneous attributes)
2. \( C $\rightarrow $ B \) (No extraneous attributes)
3. \( D $\rightarrow $ A \), \( D $\rightarrow $ B \), \( D $\rightarrow $ C \) (Decomposed from \( D $\rightarrow $ ABC \))
4. \( AC $\rightarrow $ D \) (Check if \( A \) or \( C \) is extraneous)

To check if \( A \) or \( C \) is extraneous in \( AC $\rightarrow $ D \):

- Compute the closure of \( A \) and \( C \) individually and see if they can derive \( D \).

### Step 3: Remove Redundant Dependencies

Finally, we need to check for and remove any redundant dependencies.

1. \( A $\rightarrow $ B \) (No redundancy)
2. \( C $\rightarrow $ B \) (No redundancy)
3. \( D $\rightarrow $ A \), \( D $\rightarrow $ B \), \( D $\rightarrow $ C \) (Check if any of these are redundant)
4. \( AC $\rightarrow $ D \) (Check if this is redundant)

To check for redundancy:

- Remove one dependency at a time and compute the closure of the remaining dependencies to see if the removed dependency can still be derived.

### Final Minimal Cover

After removing all extraneous attributes and redundant dependencies, the minimal cover is obtained.

From the image, the minimal cover is:

1. \( A $\rightarrow $ B \)
2. \( C $\rightarrow $ B \)
3. \( D $\rightarrow $ A \)
4. \( D $\rightarrow $ C \)
5. \( AC $\rightarrow $ D \)

The image shows the process of checking each dependency and marking them as redundant or necessary. The final minimal cover is derived by ensuring all dependencies are essential and minimal.
