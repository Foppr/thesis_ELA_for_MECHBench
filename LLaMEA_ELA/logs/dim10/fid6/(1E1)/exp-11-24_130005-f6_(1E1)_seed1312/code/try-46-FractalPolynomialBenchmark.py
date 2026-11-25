import numpy as np

class FractalPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial chaos term with varying degrees and fractal-like behavior
        poly_term = 0.0
        for i in range(self.dim):
            degree = 2 + int(3 * np.sin(x_scaled[i] * np.pi))
            poly_term += (x_scaled[i]**degree) * (1.0 + 0.3 * np.sin(5.0 * x_scaled[i]))
        
        # Fractal self-similarity component with recursive scaling
        fractal_term = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(2.0 * x_scaled[i])
            fractal_term += np.sin(scale * x_scaled[i] * 10.0) * np.cos(scale * x_scaled[i] * 7.0)
        
        # Logarithmic barrier terms creating non-smooth regions and sharp gradients
        barrier_term = 0.0
        for i in range(self.dim):
            if abs(x_scaled[i]) < 0.1:
                barrier_term += 10.0 * (1.0 / (abs(x_scaled[i]) + 0.01) - 10.0)
            else:
                barrier_term += np.log(abs(x_scaled[i]) + 0.1) * np.sin(3.0 * x_scaled[i])
        
        # Cross-dimensional coupling with polynomial interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = (x_scaled[i]**2 + x_scaled[j]**2) * (1.0 + 0.2 * np.cos(x_scaled[i] * x_scaled[j]))
                cross_term += interaction * np.sin(3.0 * x_scaled[i] + 2.0 * x_scaled[j])
        
        # Nested multimodal component with varying amplitude and frequency
        multi_term = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(x_scaled[i] * 4.0)
            freq = 2.0 + 1.5 * np.cos(x_scaled[i] * 3.0)
            multi_term += amp * np.sin(freq * x_scaled[i]) * np.exp(-x_scaled[i]**2)
        
        # Additional harmonic and chaotic modulation
        harm_term = 0.0
        for i in range(self.dim):
            harm_term += (np.sin(4.5 * x_scaled[i])**3 + 
                         0.7 * np.cos(6.2 * x_scaled[i])**2 + 
                         0.3 * np.sin(9.8 * x_scaled[i]) * np.cos(2.1 * x_scaled[i]))
        
        # Combined result with optimized weights
        return (0.4 * poly_term + 0.3 * fractal_term + 0.5 * barrier_term + 
                0.35 * cross_term + 0.45 * multi_term + 0.25 * harm_term + 1.8)