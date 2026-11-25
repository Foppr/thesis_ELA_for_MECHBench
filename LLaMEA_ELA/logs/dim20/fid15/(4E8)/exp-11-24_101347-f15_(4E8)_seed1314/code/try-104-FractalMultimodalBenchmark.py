import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term with condition number modulation
        quadratic = np.sum(x_scaled**2) * (1.0 + 0.1 * np.sin(5.0 * np.sum(x_scaled**2)))
        
        # Fractal component using iterative logistic map for self-similarity
        fractal = 0.0
        for i in range(self.dim):
            # Logistic map with parameter modulation
            r = 3.8 + 0.2 * np.sin(2.0 * x_scaled[i])
            x_logistic = 0.5
            for _ in range(10):  # Iterate to stabilize
                x_logistic = r * x_logistic * (1.0 - x_logistic)
            fractal += np.sin(10.0 * x_logistic) * np.cos(8.0 * x_logistic)
        
        # Hybrid multimodal structure with multiple peaks and valleys
        hybrid = 0.0
        for i in range(self.dim):
            # Multiple gaussian peaks with varying heights and widths
            peak_heights = [2.0, 1.5, 3.0, 2.5]
            peak_positions = [0.5, -0.7, 0.9, -0.3]
            peak_widths = [0.3, 0.4, 0.2, 0.5]
            
            for h, p, w in zip(peak_heights, peak_positions, peak_widths):
                hybrid += h * np.exp(-((x_scaled[i] - p) / w)**2)
        
        # Chaotic gradient modulation with controlled instability
        chaotic_grad = 0.0
        for i in range(self.dim):
            # Controlled chaotic sequence using sine and cosine
            seq = np.sin(15.0 * x_scaled[i]) + 0.5 * np.cos(23.0 * x_scaled[i])
            chaotic_grad += seq * np.exp(-0.5 * x_scaled[i]**2)
        
        # Cross-dimensional interaction with fractal scaling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_scaled[i] - x_scaled[j])**2 + 0.01)
                # Fractal-like interaction with scaling factor
                scale_factor = 1.0 / (1.0 + 0.5 * np.sin(10.0 * dist))
                cross_term += scale_factor * np.sin(20.0 * dist) * np.cos(15.0 * dist)
        
        # Radial fractal component with self-similar structure
        r = np.sqrt(np.sum(x_scaled**2))
        radial_fractal = np.sin(50.0 * r) * np.cos(30.0 * r) * np.exp(-r**2 / 2.0)
        
        # Combine all components with adaptive weights
        result = (quadratic + 0.8 * fractal + 1.2 * hybrid + 0.6 * chaotic_grad + 
                 0.9 * cross_term + 0.7 * radial_fractal)
        
        # Add controlled noise for increased robustness
        noise = 0.02 * np.random.normal(0.0, 1.0) * (1.0 + 0.3 * np.sin(50.0 * r))
        result += noise
        
        return result