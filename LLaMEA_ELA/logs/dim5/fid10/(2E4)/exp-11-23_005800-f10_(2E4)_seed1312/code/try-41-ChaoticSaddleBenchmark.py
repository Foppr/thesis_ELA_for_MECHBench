import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with chaotic scaling factor
        base = np.sum(x_norm**2)
        
        # Enhanced fractal-like perturbation using recursive sine waves
        fractal_pert = 0.0
        for i in range(min(6, self.dim)):
            scale = 3**(i+1)
            fractal_pert += np.sin(scale * np.pi * x_norm[i % self.dim]) * np.cos(scale * np.pi * x_norm[(i+1) % self.dim])
        
        # Modified dynamic multimodal structure based on distance from origin
        dist_from_origin = np.linalg.norm(x_norm)
        dynamic_multimodality = 0.0
        for k in range(1, 7):
            freq = k * 2.5
            dynamic_multimodality += np.sin(freq * dist_from_origin) * np.cos(freq * dist_from_origin)
        
        # Adjusted saddle-point attraction with varying strength
        saddle_attraction = 0.0
        for i in range(self.dim):
            saddle_attraction += (x_norm[i]**2 - 0.3)**2
        
        # Combined chaotic energy landscape with increased complexity
        f_val = base + 0.7 * fractal_pert + 2.5 * dynamic_multimodality + 1.8 * saddle_attraction
        
        return f_val