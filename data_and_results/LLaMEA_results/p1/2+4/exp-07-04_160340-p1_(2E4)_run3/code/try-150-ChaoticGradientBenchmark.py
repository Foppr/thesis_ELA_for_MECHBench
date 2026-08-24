import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5]
        x = x / 5.0
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add chaotic gradient components with time-varying harmonic potentials
        chaotic_gradient = 0.0
        for i in range(self.dim):
            # Time-varying harmonic potential with chaotic modulation
            t = np.sin(i * np.pi / self.dim) * np.cos(i * np.pi / (self.dim * 2.0))
            freq = 20 + 10 * np.sin(t * 10)
            amp = 0.5 + 0.3 * np.cos(t * 5)
            chaotic_gradient += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Multi-scale saddle points with varying depths
        saddle_penalty = 0.0
        for scale in [1, 2, 4]:
            for i in range(self.dim):
                # Create saddle point at different scales
                saddle_pos = np.sin(i * np.pi / self.dim) * scale
                dist = x[i] - saddle_pos
                saddle_penalty += 0.3 * dist**2 * np.exp(-dist**2 / (2.0 * scale**2))
        
        # Adaptive noise component that changes based on x values
        noise = 0.0
        for i in range(self.dim):
            # Adaptive noise with amplitude dependent on x magnitude
            noise_amp = 0.1 * (1.0 + np.abs(x[i]) / 5.0)
            noise += noise_amp * np.sin(50 * x[i] + i) * np.cos(30 * x[i] + i)
        
        # Add dynamic frequency modulation with chaotic scaling
        freq_mod = 0.0
        for i in range(self.dim):
            # Chaotic modulation using logistic map-like behavior
            logistic_val = 3.8 * (x[i] / 5.0) * (1 - (x[i] / 5.0))
            freq_mod += np.sin(15 * logistic_val) * np.cos(12 * logistic_val) * np.exp(-i / self.dim)
        
        # Multi-scale exponential decay minima
        exp_minima = 0.0
        for k in range(1, 6):
            # Create exponentially decaying minima at different scales
            scale = 1.0 / (2**k)
            # Random positions with chaotic distribution
            pos = np.sin(k * np.pi / self.dim) * scale
            exp_minima += scale * np.exp(-0.5 * ((x - pos) / (0.1 * k))**2) * np.sin(k * np.pi / 3.0)
        
        # Add spiral attractor components with chaotic rotation
        spiral_attraction = 0.0
        for i in range(self.dim):
            # Spiral pattern with chaotic phase shift
            phase = i * np.pi / (self.dim * 2.0) + np.sin(i * 0.5)
            spiral_attraction += np.sin(20 * x[i] + phase) * np.cos(15 * x[i] + phase) * np.exp(-i / (self.dim * 3.0))
        
        # Memory-dependent fitness evaluation
        memory_effect = 0.0
        if hasattr(self, 'last_x'):
            diff = np.sum((x - self.last_x)**2)
            memory_effect = 0.05 * np.exp(-diff / 5.0)
        self.last_x = x.copy()
        
        # Combine all components with proper weighting
        result += 0.5 * chaotic_gradient + 0.3 * saddle_penalty + 0.2 * noise + 0.15 * freq_mod + 0.25 * exp_minima + 0.1 * spiral_attraction + memory_effect
        
        return result