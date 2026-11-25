import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sinusoidal oscillation component
        chaotic_osc = 0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.5 * x[i] + i * 0.3)
            amp = 1.0 + 0.5 * np.cos(0.7 * x[i] + i * 0.4)
            chaotic_osc += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Polynomial conditioning with variable exponents
        poly_cond = 0
        for i in range(self.dim):
            exp_factor = 1.0 + 0.3 * np.sin(0.8 * x[i] + i * 0.2)
            poly_cond += (x[i]**(2 + exp_factor)) * np.exp(-0.1 * x[i]**2)
        
        # Exponential decay barrier terms
        barriers = 0
        for i in range(self.dim):
            dist_from_center = np.abs(x[i] - 2.0 * np.sin(i * 0.5))
            barriers += 2.0 * np.exp(-dist_from_center**2) * np.cos(3.0 * x[i])
        
        # Cross-dimensional coupling with dynamic interaction weights
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = 0.5 + 0.3 * np.sin(0.6 * (x[i] + x[j]) + i * 0.2)
                cross_coupling += weight * (x[i]**2 + x[j]**2) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Asymmetric multimodal structure with perturbed peaks
        multimodal = 0
        for i in range(self.dim):
            peak1 = np.sin(4.0 * x[i]) * np.exp(-0.2 * x[i]**2)
            peak2 = np.cos(3.0 * x[i]) * np.exp(-0.15 * x[i]**2)
            peak3 = np.sin(2.0 * x[i]**2) * np.exp(-0.1 * x[i]**2)
            multimodal += peak1 + peak2 + peak3
        
        # Global scaling factor with chaotic modulation
        global_scale = 1.5 + 0.4 * np.sin(np.sum(x) * 0.3) + 0.2 * np.cos(np.sum(x)**2 * 0.1)
        
        # Combine all components with different weights
        return global_scale * (0.3 * chaotic_osc + 0.25 * poly_cond + 0.2 * barriers + 
                              0.15 * cross_coupling + 0.1 * multimodal)