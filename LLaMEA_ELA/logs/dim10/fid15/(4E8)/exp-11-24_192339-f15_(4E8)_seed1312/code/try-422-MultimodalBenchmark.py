import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal dimensions for different scales
        self.fractal_dims = [0.3, 0.5, 0.7, 0.9, 1.1, 1.3]
        # Quantum coupling parameters
        self.quantum_couplings = np.random.uniform(0.5, 2.0, dim)
        # Dynamic saddle point positions
        self.saddle_positions = np.random.uniform(-4.0, 4.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced stochastic resonance component
        stochastic = 0.0
        for i in range(self.dim):
            # Add multi-frequency noise with quantum coupling modulation
            noise_amp = 0.2 + 0.3 * np.sin(0.4 * i + self.dim * 0.15) * self.quantum_couplings[i]
            noise = noise_amp * np.random.normal(0, 1)
            # Add chaotic modulation to the stochastic component
            chaotic_mod = 1.0 + 0.2 * np.sin(3.0 * x[i] + i * 0.5)
            stochastic += (x[i]**2 + noise)**2 * chaotic_mod
        
        # Fractal Brownian motion with dynamic scaling
        fbm = 0.0
        for scale in self.fractal_dims:
            for i in range(self.dim):
                # Multi-scale fractal contribution with adaptive weights
                pos = x[i] * scale
                adaptive_weight = 1.0 + 0.3 * np.cos(scale * pos + i * 0.2)
                fbm += adaptive_weight * np.sin(pos) * np.cos(pos**2) * (1.0 + 0.4 * np.sin(scale * pos))
        
        # Quantum mechanical potential wells with dynamic depth and position
        quantum = 0.0
        for i in range(self.dim):
            # Multiple quantum wells with time-varying depths and positions
            well_depths = [1.5, 2.5, 3.5, 4.5]
            well_positions = [-3.0, -1.0, 1.0, 3.0]
            # Dynamic modulation based on current position and dimension
            depth_mod = 1.0 + 0.2 * np.sin(x[i] * 0.5 + i * 0.3)
            pos_mod = 0.1 * np.cos(x[i] * 0.7 + i * 0.4)
            for depth, pos in zip(well_depths, well_positions):
                # Quantum potential: harmonic oscillator + perturbation with dynamic modulation
                adjusted_pos = pos + pos_mod
                potential = depth * depth_mod * (x[i] - adjusted_pos)**2 + 0.7 * np.sin(2.0 * x[i])
                quantum += np.exp(-potential)
        
        # Discontinuous gradient landscape with sharp transitions and fractal modulation
        discontinuous = 0.0
        for i in range(self.dim):
            # Sharp ridge-like transitions with fractal offset patterns
            fractal_offset = 0.3 * np.sin(i * 0.8 + self.dim * 0.4) * np.cos(i * 0.6)
            transition = np.abs(x[i] - fractal_offset) - 0.2
            discontinuous += np.maximum(0, transition)**2 * (1.0 + 0.15 * np.sin(x[i] * 2.0))
        
        # Multi-scale roughness with quantum interference patterns
        roughness = 0.0
        for i in range(self.dim):
            # Combine multiple frequency components with quantum phase modulation
            freqs = [1.0, 2.0, 4.0, 8.0, 16.0]
            amps = [1.5, 0.8, 0.5, 0.3, 0.1]
            for freq, amp in zip(freqs, amps):
                # Add quantum phase interference
                phase = np.sin(x[i] * freq * 0.5 + i * 0.3)
                roughness += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2) * (1.0 + 0.2 * phase)
        
        # Dynamic conditioning with quantum tunneling effect
        condition = 1.0 + 0.5 * np.sin(0.4 * x[0] + self.dim * 0.25) * np.cos(0.3 * x[1] + self.dim * 0.15)
        
        # Enhanced saddle point modulation with fractal dynamics
        saddle_mod = 0.0
        for i in range(self.dim):
            saddle_mod += 0.1 * np.sin(self.saddle_positions[i] * x[i]) * np.cos(x[i]**2)
        
        # Combine all components with enhanced weights and dynamic interactions
        return condition * (0.4 * stochastic + 0.25 * fbm + 
                           0.25 * quantum + 0.1 * discontinuous + 0.05 * roughness + 0.05 * saddle_mod)