import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic radial component with nested sinusoidal modulation and fractal scaling
        radius = np.sqrt(np.sum(x**2))
        if radius == 0:
            radius = 1e-10
        radial_component = (np.log(radius + 1) * 
                          np.sin(2 * radius) * 
                          np.cos(3 * radius) * 
                          np.exp(-0.2 * radius) * 
                          np.sin(0.3 * radius**2) * 
                          np.tan(0.1 * radius))
        
        # Asymmetric polynomial potentials with chaotic coefficients, mixed degrees and cross-dimensional coupling
        asym_poly = 0.0
        for i in range(self.dim):
            coeff1 = 1.5 + 0.4 * np.sin(i * 2.1)
            coeff2 = 1.1 + 0.2 * np.cos(i * 3.7)
            if x[i] >= 0:
                asym_poly += coeff1 * x[i]**6 + coeff2 * x[i]**4 + 0.2 * x[i]**3
            else:
                asym_poly += 0.8 * x[i]**5 + 0.3 * x[i]**3 + 0.1 * x[i]**2
        asym_poly /= self.dim
        
        # Enhanced trigonometric wave interference with chaotic frequencies, phase shifts and amplitude modulation
        wave_interference = 0.0
        for i in range(self.dim):
            freq = 4 * (i + 1) + 0.6 * np.sin(i * 1.2) + 0.3 * np.cos(3 * i)
            amp = 1.5 / (1.0 + i**0.7 + 0.2 * np.sin(3 * i))
            phase_shift = 0.2 * np.sin(i * 0.9 + 0.4 * np.cos(i)) 
            wave_interference += amp * np.sin(freq * x[i] + phase_shift) * np.cos(freq * x[i] * 0.9 + phase_shift)
        wave_interference /= self.dim
        
        # Cross-dimensional coupling with chaotic exponential decay, modified interaction terms and higher-order coupling
        geo_coupling = 0.0
        for i in range(self.dim - 1):
            decay_factor = np.exp(-0.3 * abs(x[i] - x[i+1])) * (1 + 0.4 * np.sin(i * 1.7))
            geo_coupling += decay_factor * np.sin(4 * (x[i] + x[i+1])) * np.cos(2 * (x[i] - x[i+1]))
        geo_coupling /= (self.dim - 1)
        
        # Multi-scale chaotic modulation with fractal-like behavior, nested sinusoidal components and chaotic perturbations
        fractal_mod = 0.0
        for i in range(self.dim):
            fractal_mod += (np.sin(6 * x[i]) * np.cos(10 * x[i]) * 
                           np.tan(0.5 * x[i]) * 
                           np.exp(-0.1 * abs(x[i])) * 
                           np.sin(0.25 * x[i]**2) * 
                           np.cos(0.3 * x[i]))
        fractal_mod /= self.dim
        
        # Asymmetric Gaussian-like local minima with shifted centers, chaotic variance and multi-modal perturbations
        gaussian_like = 0.0
        centers = np.linspace(-4.5, 4.5, self.dim)
        for i in range(self.dim):
            diff = x[i] - centers[i]
            variance = 1.5 + 0.4 * np.sin(i * 2.0)
            gaussian_like += np.exp(-0.5 * (diff / (variance + 0.2 * abs(diff)))**2) * np.cos(1.5 * diff)
        gaussian_like /= self.dim
        
        # Additional chaotic radial basis function component with modified parameters and nested coupling
        rbf_component = 0.0
        for i in range(self.dim):
            center = -4.0 + 8.0 * i / (self.dim - 1) if self.dim > 1 else 0.0
            rbf_component += np.exp(-0.5 * ((x[i] - center) / (1.5 + 0.2 * np.sin(i)))**2) * np.sin(3.0 * x[i]) * np.cos(0.5 * x[i])
        rbf_component /= self.dim
        
        # Combine all components with adjusted weights for improved fitness and complexity
        result = (asym_poly * 2.2 + wave_interference * 1.3 + 
                 geo_coupling * 1.6 + fractal_mod * 0.9 + 
                 radial_component * 0.7 + gaussian_like * 1.4 + 
                 rbf_component * 0.8)
        
        return float(result)