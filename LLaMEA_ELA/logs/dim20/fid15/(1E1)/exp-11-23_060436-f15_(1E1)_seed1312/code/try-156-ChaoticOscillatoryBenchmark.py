import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2) * 0.05
        
        # Sinusoidal oscillatory component with multiple frequencies
        oscillatory = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.3)
            oscillatory += np.sin(freq * x[i]) * np.cos(2.0 * freq * x[i])
        
        # Radial basis function component with chaotic centers
        rbf = 0
        for i in range(self.dim):
            center = 2.5 * np.sin(i * 0.4) * (1.0 + 0.1 * np.cos(i * 0.2))
            width = 0.5 + 0.3 * np.sin(i * 0.5)
            rbf += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Chaotic perturbation component using logistic map
        chaotic = 0
        r = 3.9  # Logistic map parameter
        for i in range(self.dim):
            if i == 0:
                x_prev = x[-1]
            else:
                x_prev = x[i-1]
            
            # Logistic map with input from previous dimension
            logistic = r * x_prev * (1 - x_prev)
            chaotic += np.sin(x[i] * logistic) * np.cos(x[i] + logistic)
        
        # Cross-dimensional interaction with varying coupling strengths
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = 0.5 + 0.3 * np.sin(0.2 * (i + j))
                interaction += coupling * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Multi-scale chaotic modulation
        multiscale = 0
        scales = [0.3, 0.7, 1.2, 2.0]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            multiscale += np.sin(scale * x[i]) * np.cos(scale * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Asymmetric component with chaotic modulation
        asymmetric = 0
        for i in range(self.dim):
            asym_mod = 0.2 * np.sin(0.3 * i) * np.cos(0.2 * x[i])
            asymmetric += (np.sin(x[i] + asym_mod) * np.exp(-0.1 * x[i]**2) - 
                          np.cos(x[i] + asym_mod) * np.exp(-0.15 * x[i]**2))
        
        # Multi-modal structure with dynamic peaks
        multimodal = 0
        for i in range(self.dim):
            peak_loc = 1.5 * np.sin(0.4 * i) * (1.0 + 0.1 * np.cos(i * 0.3))
            height = 0.8 + 0.4 * np.sin(0.2 * i)
            multimodal += height * (np.exp(-0.5 * (x[i] - peak_loc)**2) + 
                                  np.exp(-0.3 * (x[i] + peak_loc)**2))
        
        # Combine all components with optimized weights
        return (quadratic * 0.6 +
                oscillatory * 0.4 +
                rbf * 0.5 +
                chaotic * 0.3 +
                interaction * 0.25 +
                multiscale * 0.35 +
                asymmetric * 0.2 +
                multimodal * 0.4)