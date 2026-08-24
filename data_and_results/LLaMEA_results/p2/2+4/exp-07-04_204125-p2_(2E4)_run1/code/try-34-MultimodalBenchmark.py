import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal-like coefficients for terrain generation
        self.fractal_coeffs = np.random.uniform(-1.0, 1.0, (dim, 5))
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Fractal-like terrain with multiple scales
        for i in range(self.dim):
            # Base fractal component with varying frequency and amplitude
            for j in range(5):
                freq = 2**(j+1)
                amp = 0.5 * (0.8**(j+1))
                result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
            
            # Asymmetric saddle points with memory effect
            # Previous evaluations influence current fitness (memory effect)
            if i > 0:
                memory_factor = 0.3 * np.sin(x[i-1] * x[i])
                result += memory_factor * x[i]**2
            
            # Add cubic and quartic terms for asymmetric saddle points
            result += 0.2 * x[i]**3 + 0.05 * x[i]**4
            
            # Add aperiodic perturbations based on fractal coefficients
            perturbation = 0.0
            for j in range(5):
                perturbation += self.fractal_coeffs[i, j] * np.sin((j+1) * x[i] + j)
            result += 0.1 * perturbation
        
        # Add long-range dependencies with asymmetric coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                coupling = np.exp(-0.2 * distance) * np.sin(0.5 * (x[i] + x[j]))
                # Asymmetric coupling based on variable order
                if i < j:
                    result += 0.2 * coupling
                else:
                    result += 0.1 * coupling
        
        # Add chaotic noise with time-dependent characteristics
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x[i] * np.pi * (i+1)) * np.cos(x[i] * np.pi * (i+2))
        result += 0.05 * noise
        
        # Add non-convex, non-smooth elements with variable smoothness
        result += 0.03 * np.sum(np.abs(x)**1.3) + 0.02 * np.sum(np.sin(15.0 * x))
        
        return result