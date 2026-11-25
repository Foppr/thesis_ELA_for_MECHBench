import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for different dimensions
        self.fractal_dims = [np.log(2 * i + 1) / np.log(3) if i > 0 else 0.0 for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base quadratic term
        result += np.sum(x**2) * 0.1
        
        # Fractal-like multimodal structure using recursive sine-cosine combinations
        for i in range(self.dim):
            # Multi-scale oscillation with dynamic frequency
            freq_factor = 2 ** (i % 4)
            amp_factor = 1.0 / (1.0 + i * 0.1)
            
            # Recursive fractal component
            fractal_val = 0.0
            for k in range(1, min(6, self.dim + 1)):
                if i + k < self.dim:
                    fractal_val += amp_factor * np.sin(freq_factor * x[i]) * np.cos(freq_factor * x[i + k])
            
            result += fractal_val
            
        # Dynamic scaling based on position
        scale_factors = []
        for i in range(self.dim):
            # Use a chaotic-like scaling factor derived from sine and cosine
            scale = 1.0 + 0.5 * np.sin(x[i] * 0.7) * np.cos(x[i] * 0.3)
            scale_factors.append(scale)
        
        # Apply dynamic penalties
        for i in range(self.dim):
            # Polynomial penalty with dynamic coefficients
            result += scale_factors[i] * (0.3 * x[i]**4 + 0.2 * x[i]**3 + 0.1 * x[i]**2)
            
        # Add self-similar multi-modal peaks using a fractal-inspired approach
        for i in range(self.dim):
            # Peaks at positions that follow a fractal pattern (based on golden ratio)
            peak_positions = [5.0 * np.sin(j * 0.618) for j in range(1, 6)]
            peak_penalty = 0.0
            for pos in peak_positions:
                peak_penalty += np.exp(-0.5 * ((x[i] - pos) / 0.5)**2)
            result += 0.5 * peak_penalty
            
        # Add a global perturbation term with fractal-like characteristics
        global_perturbation = 0.0
        for i in range(self.dim):
            global_perturbation += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        result += 0.1 * global_perturbation
        
        return result