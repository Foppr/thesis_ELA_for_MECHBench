import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic component with sine and cosine interactions
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(5 * x_norm[i]) * np.cos(3 * x_norm[i])
        
        # Enhanced spiral attractor terms with radial dependence and modified angular frequency
        spiral = 0.0
        for i in range(self.dim):
            r = np.sqrt(x_norm[i]**2 + x_norm[(i+1) % self.dim]**2)
            spiral += r * np.sin(15 * np.arctan2(x_norm[i], x_norm[(i+1) % self.dim]))
        
        # Modified dynamic curvature modulation using higher-order polynomial and exponential
        curvature = 0.0
        for i in range(self.dim):
            curvature += (x_norm[i]**8 + 0.3 * np.exp(-x_norm[i]**2)) / (1.0 + np.abs(x_norm[i]))
        
        # Controlled noise sensitivity via perturbed sinusoids with altered amplitude
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(7 * x_norm[i]) * np.random.uniform(0.9, 1.1)
        
        # Altered cross-dimensional interaction with varying coupling strengths and additional quadratic terms
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += (x_norm[i]**2 + x_norm[j]**2 + 0.5 * x_norm[i] * x_norm[j]) * np.sin(x_norm[i] * x_norm[j])
        
        # Combine all components with adjusted weights
        return 0.25 * chaotic + 0.3 * spiral + 0.15 * curvature + 0.15 * noise + 0.15 * cross