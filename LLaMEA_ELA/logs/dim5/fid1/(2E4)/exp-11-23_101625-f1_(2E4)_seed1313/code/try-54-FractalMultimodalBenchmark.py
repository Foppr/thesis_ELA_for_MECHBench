import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.5 * np.sum(x**2)
        
        # Fractal-like multimodal components with self-similarity and chaotic scaling
        for i in range(self.dim):
            # Chaotic frequency progression with adaptive scaling
            freq = 3 ** (i % 5 + 1) + np.sin(i * 0.7) * 2
            # Multi-resolution interference patterns with dynamic amplitude
            amp = 0.4 * (1 + 0.1 * np.sin(i * 0.5))
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * np.log(1 + abs(x[i]))
            
        # Nested fractal valleys with varying depths and chaotic coupling
        for i in range(self.dim):
            # Create nested structures using chaotic polynomial transformations
            val = x[i]**2 + 0.1 + 0.05 * np.sin(10 * x[i])
            result += 0.5 * np.sin(15 * np.log(val)) * np.cos(7 * np.log(val)) * (1 + 0.2 * np.cos(i * 0.3))
            
        # Multi-scale ridge patterns with chaotic spacing and dynamic scaling
        for i in range(self.dim):
            # Chaotic scale ridge structure with time-varying parameters
            ridge_scale = 3 ** (i % 4 + 1) + np.cos(i * 0.4) * 1.5
            result += 0.3 * np.sin(ridge_scale * x[i]) * np.cos(ridge_scale * x[i] * 0.6) * np.exp(-0.15 * abs(x[i])) * (1 + 0.1 * np.sin(i * 0.2))
            
        # Interference terms between dimensions with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Chaotic coupling strength based on dimension indices and dynamic factors
                coupling = 0.25 * (i + j + 1) ** -0.9 * (1 + 0.1 * np.sin(i * j * 0.3))
                # Chaotic interference pattern with dynamic phase shift
                phase_shift = 0.2 * np.cos(i + j)
                result += coupling * np.sin(3**i * x[i] + phase_shift) * np.cos(3**j * x[j] + phase_shift) * np.log(1 + abs(x[i] - x[j]))
                
        # Asymmetric fractal valleys with irregular depth and chaotic scaling
        for i in range(self.dim):
            # Irregular valley structure using asymmetric chaotic polynomial
            asym_valley = (x[i]**3 + 0.6 * x[i]**2 + 0.1 * np.sin(5 * x[i])) * np.exp(-0.25 * abs(x[i]))
            result += 0.4 * asym_valley * (1 + 0.1 * np.cos(i * 0.4))
            
        # High-frequency fractal oscillations with chaotic amplitude decay
        for i in range(self.dim):
            # Fractal frequency progression with chaotic scaling factor
            freq = 15 * (i + 1) + np.sin(i * 0.6) * 5
            amp_decay = 0.15 * np.exp(-0.08 * freq) * (1 + 0.1 * np.cos(i * 0.3))
            result += amp_decay * np.sin(freq * x[i]) * np.exp(-0.07 * freq)
            
        # Enhanced chaotic noise component to increase ruggedness
        chaos_noise = 0.18 * np.sum(np.sin(x * 12) * np.cos(x * 8)) * (1 + 0.07 * np.sum(np.sin(x * 2)))
        result += chaos_noise
        
        # Additional penalty terms for improved fitness score
        penalty = 0.35 * np.sum(np.abs(x)**3.5) + 0.25 * np.sum(np.sin(5 * x)**2)
        result += penalty
        
        # Modified coupling between dimensions to improve challenge
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = 0.18 * (i + j + 1) ** -1.1 * (1 + 0.15 * np.sin(i * j * 0.4))
                result += coupling * np.sin(2**i * x[i]) * np.cos(2**j * x[j]) * np.exp(-0.1 * abs(x[i] - x[j]))
                
        return result