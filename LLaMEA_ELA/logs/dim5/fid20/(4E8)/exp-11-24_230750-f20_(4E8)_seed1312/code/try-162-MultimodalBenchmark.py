import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Composite sinusoidal waves with varying frequencies and amplitudes
        sin_wave = np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * np.exp(-0.1 * x**2))
        
        # Radial polynomial conditioning with dynamic exponents and scaling
        radial_poly = np.sum((x**2 + 0.5 * x**4 + 0.1 * x**6) * (1.0 + 0.3 * np.sin(self.dim * 0.5)))
        
        # Chaotic coupling through exponential decay with time-varying parameters
        chaotic_coupling = np.sum(np.exp(-0.5 * (x - np.sin(x))**2) * np.cos(5.0 * x))
        
        # Adaptive noise component with dynamic intensity based on dimensionality
        noise_intensity = 0.2 * (1.0 + 0.1 * self.dim)
        noise = noise_intensity * np.random.rand() * np.sum(np.sin(7.0 * x) * np.cos(3.0 * x))
        
        # Hyperbolic tangent interactions with multi-scale coupling
        tanh_interaction = np.sum(np.tanh(x[:-1] + 0.5 * x[1:]) * np.tanh(2.0 * x[:-1] - x[1:]))
        
        # Multi-modal peaks with varying heights and widths
        peak_sum = 0.0
        for i in range(min(5, self.dim)):
            center = 3.0 * np.sin(i * np.pi / 4.0)
            width = 0.8 + 0.4 * np.cos(i * np.pi / 2.0)
            height = 1.0 + 0.5 * np.sin(i * np.pi / 3.0)
            peak_sum += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Cross-terms with alternating signs and increasing complexity
        cross_terms = 0.0
        for i in range(0, self.dim - 2):
            cross_terms += (-1)**i * x[i]**3 * x[i+1]**2 * x[i+2]
        
        # Final combined function value
        return radial_poly + sin_wave + chaotic_coupling + noise + tanh_interaction + peak_sum + cross_terms