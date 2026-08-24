import numpy as np

class ExponentialWaveStochasticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with dimension-dependent scaling
        exp_component = np.sum(2.0 * np.exp(-0.5 * np.abs(x)) * np.cos(1.0 * x) * np.sin(0.5 * x))
        
        # Trigonometric wave interference with frequency modulation
        wave_interference = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(0.4 * i)
            wave_interference += np.sin(freq * x[i] + 0.2 * np.cos(0.3 * x[i])) * np.cos(freq * x[i] + 0.1 * np.sin(0.2 * x[i]))
        
        # Stochastic gradient component with adaptive noise scaling
        stochastic = 0.0
        for i in range(self.dim):
            noise_scale = 0.5 + 0.3 * np.sin(0.6 * i)
            noise = np.random.normal(0, noise_scale)
            stochastic += (x[i]**3) * np.exp(-0.1 * x[i]**2) + noise
        
        # Multi-scale harmonic modulation with varying amplitudes
        harmonic_mod = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.2 * np.sin(0.5 * i)
            freq = 2.0 + 0.5 * np.cos(0.3 * i)
            harmonic_mod += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Radial basis with exponential weighting and cross-term interactions
        radial = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                radial += np.exp(-0.2 * (x[i]**2 + x[j]**2)) * np.sin(0.3 * x[i] * x[j])
        
        # Combine all components with adaptive weighting based on dimension
        weight_exp = 1.0 + 0.1 * np.sin(0.2 * self.dim)
        weight_wave = 1.0 + 0.15 * np.cos(0.1 * self.dim)
        weight_stochastic = 1.0 + 0.05 * np.sin(0.3 * self.dim)
        weight_harmonic = 1.0 + 0.1 * np.cos(0.2 * self.dim)
        weight_radial = 1.0 + 0.08 * np.sin(0.15 * self.dim)
        
        result = weight_exp * exp_component + weight_wave * wave_interference + weight_stochastic * stochastic + weight_harmonic * harmonic_mod + weight_radial * radial
        
        return result