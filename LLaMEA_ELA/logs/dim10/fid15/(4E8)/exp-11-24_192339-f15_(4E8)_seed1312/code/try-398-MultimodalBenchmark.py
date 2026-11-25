import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal dimensions for different scales
        self.fractal_dims = [0.5, 0.7, 0.9, 1.1, 1.3]
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Stochastic gradient component with varying noise intensity
        stochastic = 0.0
        for i in range(self.dim):
            # Add Brownian motion-like perturbations with fractal scaling
            noise_amp = 0.1 + 0.2 * np.sin(0.3 * i + self.dim * 0.1)
            noise = noise_amp * np.random.normal(0, 1)
            stochastic += (x[i]**2 + noise)**2
        
        # Fractal Brownian motion component with multiple scales
        fbm = 0.0
        for scale in self.fractal_dims:
            for i in range(self.dim):
                # Multi-scale fractal contribution
                pos = x[i] * scale
                fbm += np.sin(pos) * np.cos(pos**2) * (1.0 + 0.3 * np.sin(scale * pos))
        
        # Quantum mechanical potential wells with tunable depth
        quantum = 0.0
        for i in range(self.dim):
            # Multiple quantum wells with varying depths and positions
            well_depths = [1.0, 2.0, 3.0]
            well_positions = [-3.0, 0.0, 3.0]
            for depth, pos in zip(well_depths, well_positions):
                # Quantum potential: harmonic oscillator + perturbation
                potential = depth * (x[i] - pos)**2 + 0.5 * np.sin(2.0 * x[i])
                quantum += np.exp(-potential)
        
        # Discontinuous gradient landscape with sharp transitions
        discontinuous = 0.0
        for i in range(self.dim):
            # Sharp ridge-like transitions with random offsets
            offset = 0.5 * np.sin(i * 0.7 + self.dim * 0.3)
            transition = np.abs(x[i] - offset) - 0.2
            discontinuous += np.maximum(0, transition)**2
        
        # Multi-scale roughness with exponential decay
        roughness = 0.0
        for i in range(self.dim):
            # Combine multiple frequency components with different amplitudes
            freqs = [1.0, 2.0, 4.0, 8.0]
            amps = [1.0, 0.7, 0.4, 0.2]
            for freq, amp in zip(freqs, amps):
                roughness += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Asymmetric scaling with dynamic conditioning
        condition = 1.0 + 0.5 * np.sin(0.4 * x[0] + self.dim * 0.2)
        
        # Combine all components with carefully balanced weights
        return condition * (0.3 * stochastic + 0.25 * fbm + 
                           0.25 * quantum + 0.15 * discontinuous + 0.05 * roughness)