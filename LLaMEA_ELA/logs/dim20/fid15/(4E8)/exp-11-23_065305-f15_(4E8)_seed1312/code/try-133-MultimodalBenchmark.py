import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced logarithmic radial component with chaotic modulation and multiple scales
        radius = np.sqrt(np.sum(x**2))
        if radius == 0:
            radius = 1e-10
        log_radial = (np.log(radius + 1) * 
                     np.sin(3 * radius) * 
                     np.cos(5 * radius) * 
                     np.exp(-0.1 * radius) * 
                     np.sin(0.5 * radius**2))
        
        # Asymmetric polynomial potentials with mixed degrees and chaotic coefficients
        asym_poly = 0.0
        for i in range(self.dim):
            coeff1 = 1.0 + 0.5 * np.sin(i)
            coeff2 = 0.8 + 0.2 * np.cos(i)
            if x[i] >= 0:
                asym_poly += coeff1 * x[i]**6 + coeff2 * x[i]**4 + 0.1 * x[i]**2
            else:
                asym_poly += 0.8 * x[i]**5 + 0.3 * x[i]**3 + 0.05 * x[i]
        asym_poly /= self.dim
        
        # Enhanced trigonometric wave interference with variable frequencies, amplitudes, and phase shifts
        wave_interference = 0.0
        for i in range(self.dim):
            freq = 2 * (i + 1) + np.sin(i) + 0.3 * np.cos(2 * i)
            amp = 1.0 / (1.0 + i**0.5 + 0.1 * np.sin(3 * i))
            phase_shift = 0.1 * np.sin(i * 0.5 + 0.2 * np.cos(i))  # Modified phase shift
            wave_interference += amp * np.sin(freq * x[i] + phase_shift) * np.cos(freq * x[i] * 0.7 + phase_shift)
        wave_interference /= self.dim
        
        # Cross-dimensional geometric coupling with exponential decay and chaotic modulation
        geo_coupling = 0.0
        for i in range(self.dim - 1):
            decay_factor = np.exp(-0.15 * abs(x[i] - x[i+1])) * (1 + 0.2 * np.sin(i))  # Modified decay rate
            geo_coupling += decay_factor * np.sin(2 * (x[i] + x[i+1]))
        geo_coupling /= (self.dim - 1)
        
        # Multi-scale chaotic modulation with fractal-like behavior and nested sinusoidal components
        fractal_mod = 0.0
        for i in range(self.dim):
            fractal_mod += (np.sin(7 * x[i]) * np.cos(13 * x[i]) * 
                           np.tan(0.5 * x[i]) * 
                           np.exp(-0.05 * abs(x[i])) * 
                           np.sin(0.3 * x[i]**2))
        fractal_mod /= self.dim
        
        # Asymmetric Gaussian-like local minima with shifted centers and chaotic variance
        gaussian_like = 0.0
        centers = np.linspace(-4, 4, self.dim)
        for i in range(self.dim):
            diff = x[i] - centers[i]
            variance = 1.0 + 0.5 * np.sin(i)
            gaussian_like += np.exp(-0.5 * (diff / (variance + 0.1 * abs(diff)))**2)
        gaussian_like /= self.dim
        
        # Additional chaotic radial basis function component
        rbf_component = 0.0
        for i in range(self.dim):
            center = -3.0 + 6.0 * i / (self.dim - 1) if self.dim > 1 else 0.0
            rbf_component += np.exp(-0.5 * ((x[i] - center) / (1.0 + 0.2 * np.sin(i)))**2) * np.sin(3 * x[i])
        rbf_component /= self.dim
        
        # Novel fractal-based radial component with chaotic scaling and nested modulation
        fractal_radial = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.3 * np.sin(i * 0.7) + 0.2 * np.cos(i * 0.4)
            fractal_radial += (np.sin(5 * x[i]) * np.cos(9 * x[i]) * 
                              np.exp(-0.1 * abs(x[i])) * 
                              np.sin(0.2 * x[i]**3) * 
                              scale_factor)
        fractal_radial /= self.dim
        
        # Enhanced cross-dimensional interaction with chaotic coupling coefficients
        enhanced_coupling = 0.0
        for i in range(self.dim - 1):
            coeff = 1.5 + 0.5 * np.sin(i * 0.3) + 0.3 * np.cos(i * 0.2)
            enhanced_coupling += coeff * np.sin(3 * (x[i] - x[i+1])) * np.cos(2 * (x[i] + x[i+1]))
        enhanced_coupling /= (self.dim - 1)
        
        # Combine all components with carefully adjusted weights and chaotic scaling
        result = (asym_poly * 1.8 + wave_interference * 0.9 + 
                 geo_coupling * 1.2 + fractal_mod * 0.7 + 
                 log_radial * 0.5 + gaussian_like * 1.0 + 
                 rbf_component * 0.6 + fractal_radial * 0.8 + enhanced_coupling * 0.4)
        
        return float(result)