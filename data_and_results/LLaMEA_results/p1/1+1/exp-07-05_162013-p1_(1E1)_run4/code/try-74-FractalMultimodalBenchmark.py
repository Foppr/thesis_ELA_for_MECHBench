import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal constants
        self.fractal_dim = 2.3  # Fractional dimension for fractal structure
        self.scale_factor = 0.5
        self.frequency_base = 2.0
        self.amplitude_base = 1.0
        self.chaotic_params = np.random.uniform(0.1, 0.9, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Fractal component with self-similar structure
        for i in range(self.dim):
            # Use chaotic parameters for varying scales
            scale = self.scale_factor * (1 + 0.5 * np.sin(self.chaotic_params[i] * np.pi))
            freq = self.frequency_base * (1 + 0.3 * np.cos(self.chaotic_params[i] * 2 * np.pi))
            amp = self.amplitude_base * (1 + 0.2 * np.sin(self.chaotic_params[i] * 3 * np.pi))
            
            # Fractal-like term with multiple scales
            term1 = amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
            term2 = 0.5 * amp * np.sin(freq * x[i]**3) * np.cos(freq * x[i])
            term3 = 0.3 * amp * np.sin(freq * x[i]**0.5) * np.cos(freq * x[i]**1.5)
            
            result += term1 + term2 + term3
            
        # Multi-scale trigonometric coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Scale-dependent coupling
                scale_i = 1 + 0.1 * np.sin(self.chaotic_params[i] * 5)
                scale_j = 1 + 0.1 * np.sin(self.chaotic_params[j] * 5)
                coupling = np.sin(scale_i * x[i] + scale_j * x[j])
                result += 0.1 * coupling * np.cos(2 * coupling)
                
        # Chaotic basin attraction with variable depth
        basin_depth = 0.5 + 0.3 * np.sin(self.chaotic_params[0] * 7)
        for i in range(self.dim):
            # Basin term with chaotic scaling
            basin_term = basin_depth * (x[i]**2 + 0.1 * np.sin(self.chaotic_params[i] * 10) * x[i]**3)
            result += basin_term
            
        # Add fractal dimensionality effect
        fractal_effect = 0.05 * np.sum(np.abs(x)**self.fractal_dim)
        result += fractal_effect
        
        # Add chaotic noise with fractal structure
        noise = 0.02 * np.sum(np.sin(self.chaotic_params * x) * np.cos(self.chaotic_params * x**2))
        result += noise
        
        # Add global scaling factor
        result *= (1 + 0.05 * np.sin(np.sum(x) * 0.1))
        
        return result