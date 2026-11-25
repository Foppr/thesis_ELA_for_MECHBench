import numpy as np

class FractalMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal self-similar component with multiple scales
        fractal_term = 0.0
        scales = [1.0, 0.5, 0.25, 0.125]
        for scale in scales:
            for i in range(self.dim):
                # Self-similar multimodal structure
                fractal_term += scale * (np.sin(scale * x[i]) + 
                                       0.3 * np.sin(3.0 * scale * x[i]) + 
                                       0.1 * np.sin(9.0 * scale * x[i])) * \
                               np.exp(-scale * x[i]**2 / 2.0)
        
        # Dynamic frequency modulation with chaotic component
        freq_mod = 0.0
        for i in range(self.dim):
            # Chaotic frequency modulation using logistic map-like behavior
            chaotic_factor = 1.0 + 0.5 * np.sin(x[i]) * np.cos(2.0 * x[i])
            freq_mod += (np.sin(chaotic_factor * x[i] * 2.0) + 
                        0.7 * np.cos(chaotic_factor * x[i] * 3.0)) * \
                       np.exp(-x[i]**2 / 4.0)
        
        # Scale-invariant curvature with power-law behavior
        curvature = 0.0
        for i in range(self.dim):
            # Power-law curvature with varying exponents
            curvature += (x[i]**2 + 0.2 * x[i]**3 + 0.05 * x[i]**4) * \
                        np.exp(-0.1 * np.abs(x[i]))
        
        # Cross-dimensional coupling with fractal scaling
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like coupling with scale-dependent weights
                distance = np.sqrt((x[i] - x[j])**2 + 0.1)
                weight = 1.0 / (1.0 + 0.5 * distance**1.5)
                cross_coupling += weight * np.sin(x[i] * x[j]) * \
                                 np.cos(0.5 * (x[i]**2 + x[j]**2))
        
        # Multiscale exponential interaction
        exp_interaction = 0.0
        for i in range(self.dim):
            exp_interaction += np.exp(-0.5 * x[i]**2) * \
                             (np.sin(x[i]) * np.cos(2.0 * x[i]) + 
                              0.3 * np.sin(3.0 * x[i]))
        
        # Combine all terms with dynamic weighting based on dimensionality
        dim_factor = 1.0 + 0.1 * self.dim
        result = (0.7 * fractal_term + 0.5 * freq_mod + 0.6 * curvature + 
                 0.4 * cross_coupling + 0.8 * exp_interaction) / dim_factor
        
        return result