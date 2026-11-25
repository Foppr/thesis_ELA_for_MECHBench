import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal dimensions for different scales
        self.fractal_dims = [0.4, 0.6, 0.8, 1.0, 1.2]
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Stochastic gradient component with varying noise intensity
        stochastic = 0.0
        for i in range(self.dim):
            # Add Brownian motion-like perturbations with fractal scaling
            noise_amp = 0.15 + 0.25 * np.sin(0.35 * i + self.dim * 0.12)
            noise = noise_amp * np.random.normal(0, 1)
            stochastic += (x[i]**2 + noise)**2
        
        # Fractal Brownian motion component with multiple scales
        fbm = 0.0
        for scale in self.fractal_dims:
            for i in range(self.dim):
                # Multi-scale fractal contribution
                pos = x[i] * scale
                fbm += np.sin(pos) * np.cos(pos**2) * (1.0 + 0.35 * np.sin(scale * pos))
        
        # Quantum mechanical potential wells with tunable depth
        quantum = 0.0
        for i in range(self.dim):
            # Multiple quantum wells with varying depths and positions
            well_depths = [1.2, 2.2, 3.2]
            well_positions = [-2.5, 0.0, 2.5]
            for depth, pos in zip(well_depths, well_positions):
                # Quantum potential: harmonic oscillator + perturbation
                potential = depth * (x[i] - pos)**2 + 0.6 * np.sin(2.0 * x[i])
                quantum += np.exp(-potential)
        
        # Discontinuous gradient landscape with sharp transitions
        discontinuous = 0.0
        for i in range(self.dim):
            # Sharp ridge-like transitions with random offsets
            offset = 0.4 * np.sin(i * 0.75 + self.dim * 0.35)
            transition = np.abs(x[i] - offset) - 0.15
            discontinuous += np.maximum(0, transition)**2
        
        # Multi-scale roughness with exponential decay
        roughness = 0.0
        for i in range(self.dim):
            # Combine multiple frequency components with different amplitudes
            freqs = [1.2, 2.2, 4.2, 8.2]
            amps = [1.2, 0.75, 0.45, 0.25]
            for freq, amp in zip(freqs, amps):
                roughness += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Asymmetric scaling with dynamic conditioning
        condition = 1.0 + 0.4 * np.sin(0.35 * x[0] + self.dim * 0.22)
        
        # Combine all components with carefully balanced weights
        return condition * (0.35 * stochastic + 0.20 * fbm + 
                           0.28 * quantum + 0.12 * discontinuous + 0.05 * roughness)