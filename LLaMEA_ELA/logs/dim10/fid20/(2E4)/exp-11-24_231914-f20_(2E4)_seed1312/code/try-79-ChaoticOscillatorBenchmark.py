import numpy as np

class ChaoticOscillatorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute dynamic phase shift parameters
        self.phase_shifts = np.linspace(0.1, 2.0, min(dim, 10))
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base conditioning term
        base = np.sum(x**2) / self.dim
        
        # Nested trigonometric oscillators with dynamic coupling
        oscillator = 0.0
        for i in range(self.dim):
            # Adaptive frequency based on dimension index
            freq = 1.0 + 0.5 * (i + 1) / self.dim
            phase = self.phase_shifts[i % len(self.phase_shifts)]
            
            # Nested oscillation with increasing complexity
            oscillator += (
                np.sin(freq * x[i] + phase) * 
                np.cos(freq**1.5 * x[i] + phase**2) *
                np.sin(freq**2 * x[i] + phase**3) *
                np.exp(-0.1 * np.abs(x[i]))
            )
        
        # Dynamic coupling between dimensions with varying strengths
        coupling = 0.0
        for i in range(self.dim - 1):
            # Coupling strength decreases with dimension index
            strength = 1.0 / (i + 1)
            coupling += strength * (
                np.sin(x[i] + x[i+1]) * 
                np.cos(x[i] - x[i+1]) *
                np.tan(0.5 * (x[i]**2 + x[i+1]**2)) *
                np.exp(-0.2 * (x[i]**2 + x[i+1]**2))
            )
        
        # Multi-scale chaotic modulation with exponential decay
        chaotic_mod = 0.0
        for i in range(self.dim):
            # Multiple modulation scales
            scales = [0.5, 1.0, 2.0, 3.0]
            mod = 0.0
            for scale in scales:
                mod += np.sin(scale * x[i]) * np.cos(scale**1.2 * x[i]) * np.exp(-scale * np.abs(x[i]))
            chaotic_mod += mod * np.exp(-0.15 * (i + 1))
        
        # Adaptive phase rotation with dimension-dependent weights
        phase_rotation = 0.0
        for i in range(self.dim):
            # Phase rotation based on position and dimension
            rot = np.sin(x[i]) * np.cos(x[i] * (i + 1)) * np.exp(-0.05 * x[i]**2)
            phase_rotation += rot * (i + 1) / self.dim
        
        # Combine all components with varying weights
        return base + 2.0 * oscillator + 1.5 * coupling + 1.3 * chaotic_mod + 0.8 * phase_rotation