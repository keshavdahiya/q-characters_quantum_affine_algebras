# q-characters of representations of quantum affine algebras

This project implements the Frenkel-Mukhin algorithm (https://arxiv.org/abs/math/9911112) for computing q-characters of representations of untwisted type quantum affine algebras.

## What are quantum affine algebras?

Given a lie algebra $\mathfrak{g}$, the affine algebra at level 0 (also called loop algebra) is the algebra of Laurent polynomials in one variable with values in $\mathfrak{g}$. For a simple finite dimensional Lie algebra $\mathfrak{g}$, the loop algebra $\tilde{\mathfrak{g}}$ has a presentation described by a generalized Cartan matrix of affine type. The quantum affine algebra at level 0, denoted $U_q\tilde{\mathfrak{g}}$, is a $q$-deformation of the loop algebra $\tilde{\mathfrak{g}}$. Here $q$ is a generic complex parameter.

## Finite dimensional representations of level 0 quantum affine algebras 

The infinite dimensional quantum affine algebra $U_q\tilde{\mathfrak{g}}$ at level 0, has finite dimensional representations classified by $r$-tuple of monic polynomials called Drinfeld polynomials, where $r$ is the rank of the simple finite dimensional Lie algebra $\mathfrak{g}$. 

## q-characters

The characters of representations of quantum affine algebras are called $q$-characters. Essentially, they are polynomials in variables $Y_{i,a}^{\pm 1}$, where $i\in \{1,2,\dots,r\}$ and $a\in\mathbb{C}^\times$. For simplicity we write $Y_{i,q^k}$ as $\mathrm{i}_k$.

A monomial $m$ is called dominant if does not contain variables $Y_{i,a}^{-1}$, that is, only positive powers of $Y_{i,a}$ are present in $m$. Given a dominant monomial $m$, the Frenkel-Mukhin algorithm computes the $q$-character of the representation of $U_q\tilde{\mathfrak{g}}$ having highest weight $m$. 
