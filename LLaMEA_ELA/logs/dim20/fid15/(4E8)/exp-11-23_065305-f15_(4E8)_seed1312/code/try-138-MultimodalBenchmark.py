import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic radial component with modified exponential decay and phase shifts
        radius = np.sqrt(np.sum(x**2))
        if radius == 0:
            radius = 1e-10
        radial_component = (np.log(radius + 1) * 
                          np.sin(3 * radius) * 
                          np.cos(5 * radius) * 
                          np.exp(-0.15 * radius) * 
                          np.sin(0.4 * radius**2) * 
                          (1 + 0.3 * np.sin(0.5 * radius)))
        
        # Asymmetric polynomial potentials with altered exponents and chaotic coefficients
        asym_poly = 0.0
        for i in range(self.dim):
            coeff1 = 1.2 + 0.3 * np.sin(i * 0.7)
            coeff2 = 0.9 + 0.1 * np.cos(i * 0.8)
            if x[i] >= 0:
                asym_poly += coeff1 * x[i]**5 + coeff2 * x[i]**3 + 0.15 * x[i]**2
            else:
                asym_poly += 0.9 * x[i]**4 + 0.25 * x[i]**2 + 0.08 * x[i]
        asym_poly /= self.dim
        
        # Enhanced trigonometric wave interference with modified frequencies and phase shifts
        wave_interference = 0.0
        for i in range(self.dim):
            freq = 2.5 * (i + 1) + 0.4 * np.sin(i * 0.6) + 0.2 * np.cos(3 * i)
            amp = 1.2 / (1.0 + i**0.6 + 0.15 * np.sin(2 * i))
            phase_shift = 0.15 * np.sin(i * 0.7 + 0.3 * np.cos(i * 0.4))  # Modified phase shift
            wave_interference += amp * np.sin(freq * x[i] + phase_shift) * np.cos(freq * x[i] * 0.8 + phase_shift)
        wave_interference /= self.dim
        
        # Cross-dimensional coupling with altered exponential decay and chaotic modulation
        geo_coupling = 0.0
        for i in range(self.dim - 1):
            decay_factor = np.exp(-0.2 * abs(x[i] - x[i+1])) * (1 + 0.15 * np.sin(i * 0.9))  # Modified decay rate
            geo_coupling += decay_factor * np.sin(3 * (x[i] + x[i+1]))
        geo_coupling /= (self.dim - 1)
        
        # Multi-scale chaotic modulation with nested sinusoidal components and modified amplitudes
        fractal_mod = 0.0
        for i in range(self.dim):
            fractal_mod += (np.sin(8 * x[i]) * np.cos(15 * x[i]) * 
                           np.tan(0.6 * x[i]) * 
                           np.exp(-0.07 * abs(x[i])) * 
                           np.sin(0.4 * x[i]**2))
        fractal_mod /= self.dim
        
        # Asymmetric Gaussian-like local minima with chaotic variance and shifted centers
        gaussian_like = 0.0
        centers = np.linspace(-4.5, 4.5, self.dim)
        for i in range(self.dim):
            diff = x[i] - centers[i]
            variance = 1.2 + 0.4 * np.sin(i * 0.6)
            gaussian_like += np.exp(-0.5 * (diff / (variance + 0.12 * abs(diff)))**2)
        gaussian_like /= self.dim
        
        # Additional chaotic radial basis function with altered scaling
        rbf_component = 0.0
        for i in range(self.dim):
            center = -4.0 + 8.0 * i / (self.dim - 1) if self.dim > 1 else 0.0
            rbf_component += np.exp(-0.5 * ((x[i] - center) / (1.2 + 0.15 * np.sin(i * 0.7)))**2) * np.sin(4 * x[i])
        rbf_component /= self.dim
        
        # Combine all components with adjusted weights for improved optimization characteristics
        result = (asym_poly * 2.0 + wave_interference * 1.1 + 
                 geo_coupling * 1.3 + fractal_mod * 0.8 + 
                 radial_component * 0.6 + gaussian_like * 1.1 + 
                 rbf_component * 0.7)
        
        return float(result)