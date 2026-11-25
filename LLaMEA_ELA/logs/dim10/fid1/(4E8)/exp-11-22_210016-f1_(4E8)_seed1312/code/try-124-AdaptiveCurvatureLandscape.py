import numpy as np

class AdaptiveCurvatureLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Adaptive curvature term with dynamic scaling
        curvature = 0.0
        for i in range(self.dim):
            curvature += (x[i]**2 + 0.1 * x[i]**4) * np.exp(-0.5 * x[i]**2)
        
        # Exponential polynomial component with varying exponents
        exp_poly = 0.0
        for i in range(self.dim):
            exp_poly += np.exp(-0.1 * x[i]**2) * (x[i]**3 + 0.5 * x[i]**5)
        
        # Dynamic multimodal interference with frequency modulation
        modal_interference = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.3 * np.sin(0.5 * x[i])
            modal_interference += (np.sin(freq_mod * x[i]) + 
                                0.7 * np.cos(freq_mod * x[i]**2)) * \
                               np.exp(-x[i]**2 / 8.0)
        
        # Cross-dimensional coupling with adaptive weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + 0.2 * np.abs(x[i] - x[j]))
                cross_coupling += weight * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
        
        # Gradient-based term with directional sensitivity
        gradient_term = 0.0
        for i in range(self.dim):
            gradient_term += (x[i]**2 + 0.3 * x[i]**4) * np.sin(x[i]) * np.cos(x[i])
        
        # Mixed harmonic and exponential modulation
        mixed_mod = 0.0
        for i in range(self.dim):
            mixed_mod += (np.exp(-x[i]**2) * np.sin(3.0 * x[i]) + 
                         np.cos(2.0 * x[i]) * np.exp(-0.5 * x[i]**2)) * \
                        (1.0 + 0.2 * np.sin(x[i]))
        
        # Combine all terms with dynamic weighting
        result = 0.6 * curvature + 0.4 * exp_poly + 0.7 * modal_interference + \
                 0.5 * cross_coupling + 0.3 * gradient_term + 0.8 * mixed_mod
        
        return result