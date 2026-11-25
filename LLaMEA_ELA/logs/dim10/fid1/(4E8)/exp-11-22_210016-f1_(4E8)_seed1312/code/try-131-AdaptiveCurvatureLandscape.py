import numpy as np

class AdaptiveCurvatureLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Adaptive curvature term with enhanced exponential scaling
        curvature = 0.0
        for i in range(self.dim):
            curvature += (x[i]**2 + 0.15 * x[i]**4) * np.exp(-0.3 * x[i]**2)
        
        # Exponential polynomial component with higher-order terms
        exp_poly = 0.0
        for i in range(self.dim):
            exp_poly += np.exp(-0.08 * x[i]**2) * (x[i]**4 + 0.4 * x[i]**6)
        
        # Dynamic multimodal interference with increased frequency modulation
        modal_interference = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.4 * np.sin(0.6 * x[i])
            modal_interference += (np.sin(freq_mod * x[i]) + 
                                0.8 * np.cos(freq_mod * x[i]**2)) * \
                               np.exp(-x[i]**2 / 6.0)
        
        # Cross-dimensional coupling with stronger adaptive weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + 0.3 * np.abs(x[i] - x[j]))
                cross_coupling += weight * np.sin(1.5 * x[i] * x[j]) * np.cos(1.2 * x[i] + x[j])
        
        # Gradient-based term with increased directional sensitivity
        gradient_term = 0.0
        for i in range(self.dim):
            gradient_term += (x[i]**3 + 0.4 * x[i]**5) * np.sin(x[i]) * np.cos(x[i])
        
        # Mixed harmonic and exponential modulation with altered coefficients
        mixed_mod = 0.0
        for i in range(self.dim):
            mixed_mod += (np.exp(-0.8 * x[i]**2) * np.sin(3.5 * x[i]) + 
                         np.cos(2.5 * x[i]) * np.exp(-0.6 * x[i]**2)) * \
                        (1.0 + 0.3 * np.sin(x[i]))
        
        # Combine all terms with adjusted dynamic weighting
        result = 0.7 * curvature + 0.5 * exp_poly + 0.8 * modal_interference + \
                 0.6 * cross_coupling + 0.4 * gradient_term + 0.9 * mixed_mod
        
        return result