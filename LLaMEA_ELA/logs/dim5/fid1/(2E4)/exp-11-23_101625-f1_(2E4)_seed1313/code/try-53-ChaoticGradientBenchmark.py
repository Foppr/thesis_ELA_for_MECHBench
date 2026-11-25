import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global attraction
        result = 0.1 * np.sum(x**2)
        
        # Chaotic gradient modulation with periodic attractors
        for i in range(self.dim):
            # Periodic attractor wells with chaotic positioning
            well_pos = 3 * np.sin(i * 0.5) + 2 * np.cos(i * 0.3)
            result += 0.5 * (x[i] - well_pos)**2 * (1 + 0.2 * np.sin(10 * x[i]))
            
        # Adaptive curvature components with chaotic scaling
        for i in range(self.dim):
            # Dynamic curvature based on chaotic sequence
            curvature = 2 + np.sin(i * 0.7) * 1.5 + np.cos(i * 0.4) * 0.8
            result += 0.3 * curvature * x[i]**4 * (1 + 0.1 * np.cos(5 * x[i]))
            
        # Multi-scale oscillatory terms with varying frequencies
        for i in range(self.dim):
            freq = 2**(i % 4 + 1) + 0.5 * np.sin(i * 0.6)
            result += 0.2 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * (1 + 0.1 * np.sin(x[i]))
            
        # Interdimensional coupling with chaotic phase shifts
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                phase = 0.3 * np.sin(i * j * 0.4) + 0.2 * np.cos(i + j)
                coupling_strength = 0.15 * (1 + 0.1 * np.sin(i + j))
                result += coupling_strength * np.sin(2**i * x[i] + phase) * np.cos(2**j * x[j] + phase)
                
        # Asymmetric ridge structures with chaotic amplitude
        for i in range(self.dim):
            amp = 0.4 + 0.1 * np.sin(i * 0.8)
            result += amp * np.exp(-0.5 * (x[i] - 1)**2) * np.sin(5 * x[i])
            
        # Fractal-like noise with chaotic amplitude decay
        chaos_amp = 0.1 * np.sum(np.sin(x * 7) * np.cos(x * 3))
        result += chaos_amp * (1 + 0.05 * np.sum(np.abs(x)))
        
        # Penalty terms for constraint violations and enhanced ruggedness
        penalty = 0.25 * np.sum(np.abs(x)**3) + 0.1 * np.sum(np.sin(3 * x)**2)
        result += penalty
        
        return result