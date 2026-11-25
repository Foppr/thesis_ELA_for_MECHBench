import numpy as np

class FractalMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal self-similar component with multiple scales
        fractal_term = 0.0
        scales = [1.0, 0.5, 0.25, 0.125]
        for scale in scales:
            for i in range(self.dim):
                # Enhanced multimodal structure with higher frequency components
                fractal_term += scale * (np.sin(scale * x[i]) + 
                                       0.4 * np.sin(3.0 * scale * x[i]) + 
                                       0.2 * np.sin(9.0 * scale * x[i]) + 
                                       0.05 * np.sin(27.0 * scale * x[i])) * \
                               np.exp(-scale * x[i]**2 / 2.0)
        
        # Improved dynamic frequency modulation with chaotic component
        freq_mod = 0.0
        for i in range(self.dim):
            # Enhanced chaotic frequency modulation using sine-cosine interaction
            chaotic_factor = 1.0 + 0.6 * np.sin(x[i]) * np.cos(2.0 * x[i]) + \
                            0.3 * np.sin(3.0 * x[i])
            freq_mod += (np.sin(chaotic_factor * x[i] * 2.0) + 
                        0.8 * np.cos(chaotic_factor * x[i] * 3.0) + 
                        0.2 * np.sin(chaotic_factor * x[i] * 5.0)) * \
                       np.exp(-x[i]**2 / 4.0)
        
        # Enhanced scale-invariant curvature with power-law behavior
        curvature = 0.0
        for i in range(self.dim):
            # Enhanced power-law curvature with varying exponents and interaction terms
            curvature += (x[i]**2 + 0.3 * x[i]**3 + 0.1 * x[i]**4 + 
                         0.02 * x[i]**5) * np.exp(-0.1 * np.abs(x[i]))
        
        # Improved cross-dimensional coupling with fractal scaling
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced fractal-like coupling with scale-dependent weights
                distance = np.sqrt((x[i] - x[j])**2 + 0.1)
                weight = 1.0 / (1.0 + 0.3 * distance**1.8)
                cross_coupling += weight * (np.sin(x[i] * x[j]) * 
                                          np.cos(0.5 * (x[i]**2 + x[j]**2)) + 
                                          0.1 * np.sin(2.0 * x[i] * x[j]))
        
        # Enhanced multiscale exponential interaction
        exp_interaction = 0.0
        for i in range(self.dim):
            exp_interaction += np.exp(-0.3 * x[i]**2) * \
                             (np.sin(x[i]) * np.cos(2.0 * x[i]) + 
                              0.4 * np.sin(3.0 * x[i]) + 
                              0.1 * np.sin(6.0 * x[i]))
        
        # Combine all terms with dynamic weighting based on dimensionality
        dim_factor = 1.0 + 0.15 * self.dim
        result = (0.8 * fractal_term + 0.6 * freq_mod + 0.7 * curvature + 
                 0.5 * cross_coupling + 0.9 * exp_interaction) / dim_factor
        
        return result