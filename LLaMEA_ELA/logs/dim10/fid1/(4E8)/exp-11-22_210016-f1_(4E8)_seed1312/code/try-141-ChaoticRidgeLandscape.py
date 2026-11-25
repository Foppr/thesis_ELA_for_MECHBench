import numpy as np

class ChaoticRidgeLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave components with varying frequencies and amplitudes
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.5 * i)
            amp = 1.0 + 0.3 * np.cos(0.3 * i)
            chaotic_term += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Radial basis function components with varying centers and widths
        rbf_term = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(0.4 * i)
            width = 0.5 + 0.3 * np.cos(0.6 * i)
            rbf_term += np.exp(-width * (x[i] - center)**2)
        
        # Asymmetric elliptic curvature with directional sensitivity
        elliptic_term = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                elliptic_term += 0.5 * x[i]**2 + 0.1 * x[i]**4
            else:
                elliptic_term += 0.3 * x[i]**2 + 0.2 * x[i]**4
        
        # Cross-dimensional coupling with asymmetric interaction weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i % 2 == 0:
                    weight = 1.0 + 0.5 * np.sin(0.3 * x[i])
                else:
                    weight = 1.0 + 0.3 * np.cos(0.4 * x[j])
                cross_term += weight * np.sin(x[i] * x[j]) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        # Sharp ridge components with exponential decay
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_term += np.exp(-0.5 * (x[i] - 1.0)**2) * np.sin(3.0 * x[i]) + \
                         np.exp(-0.3 * (x[i] + 2.0)**2) * np.cos(2.0 * x[i])
        
        # Combined function with dynamic weighting
        result = 0.8 * chaotic_term + 0.6 * rbf_term + 0.7 * elliptic_term + \
                 0.5 * cross_term + 0.9 * ridge_term
        
        return result