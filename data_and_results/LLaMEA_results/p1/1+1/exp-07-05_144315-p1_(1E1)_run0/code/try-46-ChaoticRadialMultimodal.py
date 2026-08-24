import numpy as np

class ChaoticRadialMultimodal:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis functions with periodic modulation
        rbfs = 0.0
        centers = np.linspace(-4.0, 4.0, 9)
        for i, center in enumerate(centers):
            for j, c in enumerate(centers):
                if i == 0 and j == 0:
                    continue
                dist = np.sqrt((x[0] - center)**2 + (x[1] - c)**2)
                rbfs += np.exp(-0.5 * dist**2) * np.sin(2 * np.pi * dist)
        
        # Polynomial interactions with chaotic perturbations
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j])
        
        # Chaotic perturbation using logistic map
        chaotic = 0.0
        r = 3.95
        for i in range(self.dim):
            chaotic += np.sin(r * np.sin(x[i]) * (1 - np.sin(x[i])))
        
        # Cross-dimensional sinusoidal coupling
        coupling = 0.0
        for i in range(self.dim):
            coupling += np.sin(x[i]) * np.cos(x[(i+1) % self.dim])
        
        # Add quartic and cubic terms for nonlinearity
        quartic = 0.01 * np.sum(x**4)
        cubic = 0.05 * np.sum(x**3)
        
        # Distance-based scaling with chaotic modulation
        distance = np.sqrt(np.sum(x**2))
        scaling = 1.0 + 0.3 * np.sin(0.5 * distance) * np.cos(0.3 * distance)
        
        return rbfs + 0.7 * poly_interaction + 0.3 * chaotic + 0.5 * coupling + cubic + quartic + scaling