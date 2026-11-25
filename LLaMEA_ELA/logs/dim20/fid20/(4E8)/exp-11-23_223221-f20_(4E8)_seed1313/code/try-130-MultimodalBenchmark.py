import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic trigonometric base with adaptive frequencies
        trig_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.7)
            trig_term += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive Gaussian ridge structures with cross-dimensional coupling
        ridge_term = 0.0
        for i in range(self.dim):
            # Gaussian ridge with adaptive width and height
            width = 1.0 + 0.3 * np.cos(i * 0.5)
            height = 0.8 + 0.2 * np.sin(i * 0.3)
            ridge = height * np.exp(-0.5 * (x[i] / width)**2)
            
            # Cross-dimensional coupling with neighbor influence
            coupling = 0.0
            for j in range(max(0, i-1), min(self.dim, i+2)):
                if i != j:
                    coupling += np.exp(-0.2 * (x[i] - x[j])**2) * np.sin(x[i] + x[j])
            
            ridge_term += ridge * (1.0 + 0.5 * coupling)
        
        # Multi-scale fractal-like interaction terms
        fractal_term = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.4 * np.sin(2.0 * i)
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                # Fractal-like interaction with logarithmic scaling
                fractal_term += (scale_factor / (dist + 0.1)) * np.sin(5.0 * dist) * np.cos(3.0 * dist)
        
        # Deceptive polynomial basin with varying curvature
        basin_term = 0.0
        for i in range(self.dim):
            # Varying polynomial exponents based on dimension index
            exp1 = 2.0 + 0.5 * np.sin(i * 0.8)
            exp2 = 4.0 + 0.3 * np.cos(i * 0.6)
            basin_term += (0.5 * x[i]**exp1 + 0.3 * x[i]**exp2 + 
                          0.2 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]))
        
        # Chaotic perturbation with exponential decay
        chaotic_term = 0.0
        for i in range(self.dim):
            # Add chaotic modulation with varying intensity
            intensity = 0.5 + 0.3 * np.sin(i * 1.1)
            chaotic_term += intensity * np.sin(10.0 * x[i]) * np.exp(-0.2 * np.abs(x[i]))
        
        # Global scaling and regularization
        global_term = 0.0
        for i in range(self.dim):
            global_term += (0.7 * x[i]**3 + 0.2 * x[i]**5 + 
                           0.1 * np.log(np.abs(x[i]) + 2.0) + 
                           0.3 * np.sin(4.0 * x[i]))
        
        # Add noise to increase landscape irregularity
        noise = 0.03 * np.sum(np.sin(8.0 * x) * np.cos(6.0 * x))
        
        # Return combined function value
        return trig_term + ridge_term + fractal_term + basin_term + chaotic_term + global_term + noise + 0.005 * np.sum(x**2)