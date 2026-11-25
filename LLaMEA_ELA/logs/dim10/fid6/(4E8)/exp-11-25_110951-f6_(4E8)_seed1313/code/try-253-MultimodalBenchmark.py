import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        
        # Asymmetric elliptic components with multi-scale sinusoidal modulations
        for i in range(self.dim):
            # Primary elliptic term with asymmetric scaling and exponential potential
            ellipse_term = (x_norm[i]**2 + 0.3 * np.exp(-5 * np.abs(x_norm[i])) * np.sin(5 * x_norm[i])**2) / (1.0 + 0.1 * np.abs(x_norm[i]))
            
            # Multi-scale periodic wave interference pattern
            wave1 = np.sin(10 * x_norm[i])
            wave2 = np.cos(15 * x_norm[i])
            wave3 = np.sin(25 * x_norm[i])
            wave4 = np.cos(35 * x_norm[i])
            
            # Multi-scale modulation with dynamic amplitude
            interference = (wave1 + 0.7 * wave2 + 0.3 * wave3 + 0.2 * wave4) / (1.0 + 0.05 * x_norm[i]**2)
            
            result += ellipse_term + interference
            
        # Enhanced cross-dimensional coupling with fractal basins and exponential weighting
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric coupling with phase shift, exponential weighting, and fractal-like interaction
                diff = x_norm[i] - x_norm[j]
                sum_val = x_norm[i] + x_norm[j]
                
                # Fractal basin effect with dynamic weighting
                weight = 0.5 * (1 + np.tanh(diff)) * np.exp(-0.5 * np.abs(diff))
                
                # Multi-scale interaction terms for increased complexity
                coupling += weight * (np.sin(8 * diff) * np.cos(6 * sum_val) * 
                                    np.exp(-0.2 * (diff**2 + sum_val**2)) + 
                                    0.3 * np.sin(12 * diff) * np.cos(9 * sum_val) * 
                                    np.exp(-0.1 * (diff**2 + sum_val**2)))
        
        # Add enhanced coupling term with scaling factor
        result += 0.4 * coupling
        
        # High-frequency noise-like component with exponential modulation for increased complexity
        noise = 0.0
        for i in range(self.dim):
            noise += (0.5 * np.sin(40 * x_norm[i]) + 
                     0.3 * np.cos(60 * x_norm[i]) + 
                     0.2 * np.sin(80 * x_norm[i]) +
                     0.1 * np.cos(100 * x_norm[i]))
        
        # Global scaling with exponential decay based on distance from origin and fractal-like behavior
        global_scale = 1.0 + 0.5 * np.exp(-0.1 * np.sum(x_norm**2)) * (1.0 + 0.2 * np.sin(5 * np.sum(x_norm**2)))
        
        return result * global_scale + 0.2 * noise