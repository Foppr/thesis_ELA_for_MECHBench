import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Chaotic tent map multimodal component with varying parameters
        tent = 0
        for i in range(self.dim):
            a = 1.5 + 0.5 * np.sin(i)
            if x[i] < a:
                tent += 0.3 * (x[i] / a)**2
            else:
                tent += 0.3 * ((1 - x[i]) / (1 - a))**2
        
        # Adaptive Gaussian RBF with dynamic widths and centers
        rbf = 0
        for i in range(self.dim):
            center = 5.0 * np.sin(i * np.pi / self.dim)
            width = 0.5 + 0.5 * np.cos(i * np.pi / self.dim)
            rbf += 0.4 * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Dynamic sine-cosine coupling with fractal-like self-similarity
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling += 0.2 * np.sin(x[i]) * np.cos(x[j]) * np.sin(3 * x[i] + 2 * x[j])
        
        # Fractal-like cross-dimensional interaction with power scaling
        fractal = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i + j < self.dim:
                    fractal += 0.15 * (x[i] ** (1 + 0.2 * np.sin(i))) * (x[j] ** (1 + 0.3 * np.cos(j)))
        
        # Dynamic conditioning with exponential scaling
        cond = 0
        for i in range(self.dim):
            cond += 0.25 * np.exp(0.1 * x[i]**2) * np.sin(2 * x[i])
        
        # Multi-scale oscillation component with varying frequencies
        multi_scale = 0
        for i in range(self.dim):
            freqs = [7, 11, 13, 17]
            multi_scale += 0.3 * sum(np.sin(freq * x[i]) for freq in freqs[:min(i+1, len(freqs))])
        
        # Combined function with enhanced complexity and difficulty
        return sphere + 0.5 * (tent + rbf + coupling + fractal + cond + multi_scale)