import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive conditioning parameters
        self.conditioning = [np.random.uniform(0.5, 2.0) for _ in range(dim)]
        self.oscillation_freq = [np.random.uniform(1.0, 3.0) for _ in range(dim)]
        self.local_minima = np.random.uniform(-4.0, 4.0, (5, dim))
        self.time_phase = np.random.rand() * 2 * np.pi
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with adaptive conditioning
        radial = 0
        for i in range(self.dim):
            cond = self.conditioning[i]
            radial += cond * (x[i]**2) / (1.0 + cond * np.abs(x[i]))
            
        # Periodic oscillation component with time-varying frequency
        periodic = 0
        for i in range(self.dim):
            freq = self.oscillation_freq[i]
            time_factor = np.sin(self.time_phase + x[i] * freq)
            periodic += np.sin(x[i] * freq) * (1.0 + 0.3 * time_factor)
            
        # Multiple local minima with adaptive weights
        minima = 0
        for i in range(5):
            weight = 1.0 / (1.0 + np.sum((x - self.local_minima[i])**2) * 0.1)
            minima += weight * np.exp(-np.sum((x - self.local_minima[i])**2) * 0.5)
            
        # Cross-dimensional coupling with radial distance modulation
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                coupling += (dist / (1.0 + dist)) * np.sin(self.time_phase + dist * 2.0)
                
        # Chaotic noise with time-dependent amplitude
        noise_amp = 0.5 * (1.0 + 0.3 * np.cos(self.time_phase * 1.7))
        noise = noise_amp * np.random.uniform(-0.5, 0.5)
        
        # Combine all components with dynamic weighting
        result = 1.2 * radial + 0.8 * periodic + 1.5 * minima + 0.6 * coupling + 0.3 * noise
        
        # Add dimensionality scaling factor
        dim_factor = np.sin(self.time_phase + self.dim * 0.7) * 0.4 + 0.6
        result *= (1.0 + 0.2 * dim_factor)
        
        return result