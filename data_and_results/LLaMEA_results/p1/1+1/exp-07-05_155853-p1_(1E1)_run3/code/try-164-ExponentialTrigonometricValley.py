import numpy as np

class ExponentialTrigonometricValley:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay components with varying rates
        exp_decay = 0
        for i in range(self.dim):
            rate = 0.1 + 0.4 * np.sin(i * 0.5) + 0.2 * np.cos(i * 0.3)
            exp_decay += np.exp(-rate * np.abs(x[i])) * np.sin(x[i])**2
        
        # Trigonometric wave interference with dynamic amplitudes
        wave_interf = 0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i * 0.7)
            wave_interf += amp * np.sin(2.0 * np.pi * x[i] + i * 0.3) * np.cos(2.0 * np.pi * x[i] + i * 0.5)
        
        # Adaptive parabolic valleys with shifting centers
        parab_valley = 0
        for i in range(self.dim):
            center = -3.0 + 6.0 * (i / max(1, self.dim - 1)) + 0.5 * np.sin(i * 0.9)
            width = 0.5 + 0.5 * np.abs(np.cos(i * 0.4))
            parab_valley += (x[i] - center)**2 * np.exp(-0.5 * (x[i] - center)**2 / width**2)
        
        # Dynamic conditioning with chaotic scaling factors
        cond_factor = 0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(i * 0.6) + 0.2 * np.cos(i * 0.8)
            cond_factor += scale * x[i]**2
        
        # Cross-dimensional coupling with exponential weights
        cross_coupling = 0
        for i in range(self.dim - 1):
            weight = 0.5 + 0.5 * np.exp(-0.1 * i) * np.sin(i * 0.4)
            cross_coupling += weight * np.exp(-0.5 * (x[i] - x[i+1])**2)
        
        # Sine-cosine hybrid modulation
        modulator = np.sin(0.2 * np.sum(x)) * np.cos(0.1 * np.sum(x**2)) + 0.5 * np.sin(0.3 * np.sum(x**3))
        
        # Add a new chaotic oscillation term for enhanced ruggedness
        chaos_term = 0
        for i in range(self.dim):
            freq = 1.0 + 0.2 * np.sin(i * 0.8)
            chaos_term += np.sin(freq * x[i]) * np.cos(freq * x[i]**3)
        
        # Combine all components with refined weights
        return 1.2 * exp_decay + 0.8 * wave_interf + 0.6 * parab_valley + 0.3 * cond_factor + 0.2 * cross_coupling + 0.1 * modulator + 0.08 * chaos_term