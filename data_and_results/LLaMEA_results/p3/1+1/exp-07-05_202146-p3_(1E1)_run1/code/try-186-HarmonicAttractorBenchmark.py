import numpy as np

class HarmonicAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize harmonic coefficients for each dimension
        self.harmonic_coeffs = np.array([np.sin(i * 0.31) * np.cos(i * 0.57) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Multi-modal periodic components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.42)
            amp = 1.5 + 0.5 * np.cos(i * 0.33)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            
        # Cross-dimensional harmonic interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                result += 0.3 * interaction * np.exp(-0.05 * (i + j))
                
        # Global minimum attractor with logarithmic barrier
        result += 0.2 * np.sum(np.log(1.0 + np.abs(x))) + 0.1 * np.prod(np.cos(0.5 * x))
        
        # Complex harmonic attractor with dynamic phase
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.1 * i))
        result += 0.4 * np.sin(phase_sum * 2.0) * np.cos(phase_sum * 0.7)
        
        # Multi-scale fractal-like oscillations
        for i in range(self.dim):
            result += 0.15 * np.sin(5.0 * x[i]) * np.cos(2.5 * x[i]) * np.exp(-0.03 * x[i]**2)
            
        # Memory-dependent harmonic influence
        if hasattr(self, 'history'):
            memory_influence = 0.0
            for i in range(self.dim):
                memory_influence += 0.08 * self.history[i] * np.sin(x[i] * 0.6)
            result += memory_influence
        self.history = x.copy()
        
        # Add a complex multi-modal structure with chaotic frequency modulation
        modal_term = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.5 * np.sin(x[i] * 0.3)
            modal_term += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i] * 0.4)
        result += 0.25 * modal_term
        
        # Fractal-like harmonic structure with self-similarity
        fractal_harmonic = 0.0
        for i in range(self.dim):
            fractal_harmonic += self.harmonic_coeffs[i] * np.sin(4.0 * x[i]) * np.cos(2.0 * x[i])
        result += 0.18 * fractal_harmonic
        
        # Add a high-frequency noise component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(15.0 * x[i]) * np.cos(7.5 * x[i])
        result += noise
        
        return result