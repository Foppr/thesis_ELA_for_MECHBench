import numpy as np

class AdaptiveCurvatureLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced adaptive curvature with stronger polynomial components
        curvature = 0.0
        for i in range(self.dim):
            curvature += (x[i]**2 + 0.2 * x[i]**4 + 0.05 * x[i]**6) * np.exp(-0.3 * x[i]**2)
        
        # Modified exponential polynomial with higher-order terms and altered weights
        exp_poly = 0.0
        for i in range(self.dim):
            exp_poly += (np.exp(-0.15 * x[i]**2) * (x[i]**3 + 0.4 * x[i]**5 + 0.1 * x[i]**7))
        
        # Improved dynamic multimodal interference with enhanced frequency modulation
        modal_interference = 0.0
        for i in range(self.dim):
            freq_mod = 1.2 + 0.4 * np.sin(0.7 * x[i])
            modal_interference += (np.sin(freq_mod * x[i]) + 
                                0.8 * np.cos(freq_mod * x[i]**2) + 
                                0.3 * np.sin(2.0 * freq_mod * x[i])) * \
                               np.exp(-x[i]**2 / 6.0)
        
        # Enhanced cross-dimensional coupling with nonlinear weight functions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + 0.3 * np.abs(x[i] - x[j])**1.5)
                cross_coupling += weight * (np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) + 
                                          0.2 * np.sin(x[i]**2 + x[j]**2))
        
        # Enhanced gradient-based term with increased directional sensitivity
        gradient_term = 0.0
        for i in range(self.dim):
            gradient_term += (x[i]**2 + 0.4 * x[i]**4 + 0.1 * x[i]**6) * np.sin(x[i]) * np.cos(x[i])
        
        # Refined mixed harmonic and exponential modulation with additional sinusoidal components
        mixed_mod = 0.0
        for i in range(self.dim):
            mixed_mod += (np.exp(-x[i]**2) * np.sin(3.0 * x[i]) + 
                         np.cos(2.0 * x[i]) * np.exp(-0.5 * x[i]**2) + 
                         0.5 * np.sin(5.0 * x[i]) * np.exp(-0.2 * x[i]**2)) * \
                        (1.0 + 0.3 * np.sin(x[i]) + 0.1 * np.cos(2.0 * x[i]))
        
        # Combine all terms with updated weighting scheme for better balance
        result = 0.7 * curvature + 0.5 * exp_poly + 0.8 * modal_interference + \
                 0.6 * cross_coupling + 0.4 * gradient_term + 0.9 * mixed_mod
        
        return result