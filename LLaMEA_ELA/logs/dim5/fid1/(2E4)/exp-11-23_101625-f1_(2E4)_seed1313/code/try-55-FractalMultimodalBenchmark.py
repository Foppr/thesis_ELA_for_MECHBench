import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.5 * np.sum(x**2)
        
        # Enhanced fractal-like multimodal components with self-similarity and chaotic scaling
        for i in range(self.dim):
            # Chaotic frequency progression with adaptive scaling
            freq = 4 ** (i % 6 + 1) + np.sin(i * 0.8) * 2.5
            # Multi-resolution interference patterns with dynamic amplitude
            amp = 0.5 * (1 + 0.15 * np.sin(i * 0.6))
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.4) * np.log(1 + abs(x[i]))
            
        # Nested fractal valleys with varying depths and chaotic coupling
        for i in range(self.dim):
            # Create nested structures using chaotic polynomial transformations
            val = x[i]**2 + 0.15 + 0.07 * np.sin(12 * x[i])
            result += 0.6 * np.sin(18 * np.log(val)) * np.cos(8 * np.log(val)) * (1 + 0.25 * np.cos(i * 0.35))
            
        # Multi-scale ridge patterns with chaotic spacing and dynamic scaling
        for i in range(self.dim):
            # Chaotic scale ridge structure with time-varying parameters
            ridge_scale = 4 ** (i % 5 + 1) + np.cos(i * 0.45) * 2.0
            result += 0.35 * np.sin(ridge_scale * x[i]) * np.cos(ridge_scale * x[i] * 0.7) * np.exp(-0.2 * abs(x[i])) * (1 + 0.15 * np.sin(i * 0.25))
            
        # Interference terms between dimensions with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                # Chaotic coupling strength based on dimension indices and dynamic factors (mutated)
                coupling = 0.3 * (i + j + 1) ** -1.2 * (1 + 0.2 * np.sin(i * j * 0.4))
                # Chaotic interference pattern with dynamic phase shift
                phase_shift = 0.3 * np.cos(i + j)
                result += coupling * np.sin(4**i * x[i] + phase_shift) * np.cos(4**j * x[j] + phase_shift) * np.log(1 + abs(x[i] - x[j]))
                
        # Asymmetric fractal valleys with irregular depth and chaotic scaling
        for i in range(self.dim):
            # Irregular valley structure using asymmetric chaotic polynomial (mutated)
            asym_valley = (x[i]**3 + 0.7 * x[i]**2 + 0.15 * np.sin(6 * x[i])) * np.exp(-0.3 * abs(x[i]))
            result += 0.45 * asym_valley * (1 + 0.18 * np.cos(i * 0.45))
            
        # High-frequency fractal oscillations with chaotic amplitude decay
        for i in range(self.dim):
            # Fractal frequency progression with chaotic scaling factor (mutated)
            freq = 22 * (i + 1) + np.sin(i * 0.65) * 6
            amp_decay = 0.22 * np.exp(-0.1 * freq) * (1 + 0.18 * np.cos(i * 0.35))
            result += amp_decay * np.sin(freq * x[i]) * np.exp(-0.12 * freq)
            
        # Additional chaotic noise component to increase ruggedness (mutated)
        chaos_noise = 0.18 * np.sum(np.sin(x * 13) * np.cos(x * 8)) * (1 + 0.08 * np.sum(np.sin(x)))
        result += chaos_noise
        
        return result