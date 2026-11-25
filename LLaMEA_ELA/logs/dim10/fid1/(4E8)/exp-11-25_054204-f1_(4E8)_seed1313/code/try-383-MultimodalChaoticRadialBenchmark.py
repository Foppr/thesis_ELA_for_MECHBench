import numpy as np

class MultimodalChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for phase modulation
        self.chaotic_phase = np.sin(np.arange(1, dim + 1) * np.pi / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with chaotic scaling
        rbf_sum = 0.0
        for i in range(self.dim):
            r = np.sqrt(np.sum(x**2))
            phase = self.chaotic_phase[i]
            rbf_sum += np.exp(-0.5 * (x[i] - phase)**2) * np.sin(3.0 * r + phase)
        
        # Dynamic polynomial component with time-varying exponents
        poly_sum = 0.0
        for i in range(self.dim):
            exp_factor = 1.0 + 0.5 * np.sin(i * 0.7 + np.sum(x**2) / 10.0)
            poly_sum += (x[i]**(2.0 + exp_factor)) * np.cos(2.0 * x[i])
        
        # Cross-dimensional coupling with sine modulation
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            coupling_strength = 0.3 * (1.0 + np.sin(i * 0.5))
            cross_coupling += coupling_strength * np.sin(x[i] + x[i+1])
        
        # Chaotic harmonic component with dynamic frequency
        freq_mod = 2.0 + 1.5 * np.sin(np.sum(x**2) / 20.0)
        chaotic_harmonic = 0.0
        for i in range(self.dim):
            chaotic_harmonic += np.sin(freq_mod * x[i] + self.chaotic_phase[i])
        
        # Radial sinusoidal component with dynamic amplitude
        radial_amp = 1.0 + 0.3 * np.cos(np.sum(x**2) / 15.0)
        radial_sin = radial_amp * np.sum(np.sin(x) * np.cos(1.5 * x))
        
        # Exponential decay with chaotic modulation
        exp_decay = 0.0
        for i in range(self.dim):
            exp_decay += np.exp(-0.1 * (x[i] - self.chaotic_phase[i])**2) * np.sin(4.0 * x[i])
        
        # Polynomial chaos with dynamic coefficients
        poly_chaos = 0.0
        for i in range(self.dim):
            coeff = 0.5 + 0.3 * np.sin(i * 0.8 + np.sum(x**2) / 12.0)
            poly_chaos += coeff * x[i]**4
        
        # Sine-cosine coupling with chaotic weights
        sine_cosine = 0.0
        for i in range(self.dim):
            weight = 0.4 + 0.2 * np.cos(i * 0.6 + np.sum(x**2) / 10.0)
            sine_cosine += weight * np.sin(x[i]) * np.cos(2.0 * x[i])
        
        # Additional multimodal term with fractal-like behavior
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(5.0 * x[i] + np.sin(3.0 * x[i])) * np.cos(2.0 * x[i])
        
        # Combined function with dimensionality-dependent scaling
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return scale_factor * (rbf_sum + poly_sum + cross_coupling + chaotic_harmonic + 
                              radial_sin + exp_decay + poly_chaos + sine_cosine + fractal_term)