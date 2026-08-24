import numpy as np

class ChaoticFourierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic constants
        self.r = 3.9  # Logistic map parameter
        self.freqs = np.arange(1, dim + 1) * 2  # Frequency multipliers
        self.amps = np.arange(1, dim + 1) * 0.5  # Amplitude multipliers
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize with quadratic basin
        f_value = np.sum(x**2) * 0.1
        
        # Add chaotic logistic map component
        chaotic_term = 0.0
        x_prev = x.copy()
        for _ in range(5):  # Iterate chaotic map 5 times
            x_new = self.r * x_prev * (1 - x_prev)
            chaotic_term += np.sum((x_new - x_prev)**2)
            x_prev = x_new
        f_value += 0.5 * chaotic_term
        
        # Add Fourier series with chaotic modulation
        fourier_sum = 0.0
        for i in range(self.dim):
            # Use chaotic sequence to modulate frequencies
            freq_mod = (np.sin(i * 0.7) + 1.0) * 0.5 + 1.0
            amp_mod = (np.cos(i * 0.3) + 1.0) * 0.5 + 0.5
            fourier_sum += amp_mod * (np.sin(freq_mod * self.freqs[i] * x[i]) + 
                                    np.cos(freq_mod * self.freqs[i] * x[i]))
        f_value += 0.3 * fourier_sum
        
        # Add polynomial chaos with sinusoidal coupling
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x[i]**5 + x[i]**3) * np.sin(2 * x[i]) * np.cos(3 * x[i])
        f_value += 0.2 * poly_chaos
        
        # Add cross-dimensional chaotic interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling with phase shift
                phase = np.sin(x[i] * x[j]) + np.cos(x[i] + x[j])
                cross_term += np.sin(2 * x[i] + x[j] + phase) * np.cos(x[i] - x[j] + phase)
        f_value += 0.4 * cross_term
        
        # Add multi-scale sinusoidal modulation
        scale_term = 0.0
        for i in range(self.dim):
            scale_term += np.sin(10 * x[i]) * np.cos(15 * x[i]) * np.sin(20 * x[i])
        f_value += 0.3 * scale_term
        
        # Add a global chaotic attractor component
        attractor = 0.0
        for i in range(self.dim):
            attractor += np.sin(x[i] * 10) * np.cos(x[i] * 15) * np.sin(x[i] * 20)
        f_value += 0.25 * attractor
        
        # Add noise for irregularity
        noise = np.random.normal(0, 0.05, self.dim)
        f_value += 0.1 * np.sum(noise * x)
        
        return f_value