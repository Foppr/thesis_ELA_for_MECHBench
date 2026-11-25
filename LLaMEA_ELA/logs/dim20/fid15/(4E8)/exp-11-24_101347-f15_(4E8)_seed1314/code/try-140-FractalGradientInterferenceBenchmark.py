import numpy as np

class FractalGradientInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors and interference parameters
        self.fractal_scales = np.logspace(-2, 1, min(5, dim), base=10)
        self.interference_freqs = np.logspace(0, 2, min(4, dim), base=10)
        self.gradient_modulators = np.linspace(0.5, 2.0, min(3, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base fractal-like quadratic term with hierarchical scaling
        base = np.sum(x_norm**2) * (1.0 + 0.2 * np.sin(np.sum(x_norm**3)))
        
        # Multi-scale fractal component with hierarchical structure
        fractal = 0.0
        for i in range(self.dim):
            scale = self.fractal_scales[min(i, len(self.fractal_scales)-1)]
            # Fractal-like sine waves with varying frequencies and amplitudes
            for k in range(1, min(6, int(scale * 10))):
                freq = k * scale * 5.0
                amp = 1.0 / (k + 1) * scale
                fractal += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]**2)
        
        # Dynamic gradient modulation with scale-dependent characteristics
        gradient_mod = 0.0
        for i in range(self.dim):
            modulator = self.gradient_modulators[min(i, len(self.gradient_modulators)-1)]
            # Create dynamic gradient field
            grad_field = np.sin(x_norm[i] * modulator * 3.0) * np.cos(x_norm[i] * modulator * 7.0)
            gradient_mod += grad_field * (1.0 + 0.3 * np.sin(x_norm[i]**2))
        
        # Cross-dimensional interference patterns
        interference = 0.0
        for i in range(self.dim):
            freq = self.interference_freqs[min(i, len(self.interference_freqs)-1)]
            for j in range(i+1, min(i+3, self.dim)):
                # Interference between dimensions with frequency-dependent coupling
                coupling = np.sin(freq * (x_norm[i] + x_norm[j])) * np.cos(freq * (x_norm[i] - x_norm[j]))
                interference += coupling * (1.0 + 0.2 * np.sin(3.0 * (x_norm[i]**2 + x_norm[j]**2)))
        
        # Asymmetric ridge structure with scale-dependent complexity
        asymmetric = 0.0
        for i in range(self.dim):
            # Create asymmetric ridges using polynomial transformations
            asym_term = (x_norm[i]**3 + 0.5 * x_norm[i]**5) * np.cos(2.0 * x_norm[i])
            asymmetric += asym_term * (1.0 + 0.4 * np.sin(x_norm[i]))
        
        # Multi-scale periodic component with varying amplitudes
        periodic = 0.0
        for i in range(self.dim):
            scale = self.fractal_scales[min(i, len(self.fractal_scales)-1)]
            # Add periodic components with scale-dependent frequencies
            for k in range(1, min(4, int(scale * 8))):
                freq = k * scale * 8.0
                periodic += np.sin(freq * x_norm[i]) * (1.0 / (k + 2)) * (1.0 + 0.3 * np.cos(freq * x_norm[i]**2))
        
        # Position-dependent conditioning with fractal characteristics
        condition_factor = 1.0 + 0.5 * np.sin(np.sum(x_norm**4) * 2.0)
        
        # Combine all components with dynamic weighting based on position
        result = (base * condition_factor +
                 1.5 * fractal +
                 0.8 * gradient_mod +
                 1.2 * interference +
                 0.6 * asymmetric +
                 0.9 * periodic)
        
        # Add fractal noise with self-similar characteristics
        noise_amp = 0.02 * (1.0 + 0.3 * np.sin(np.sum(x_norm**2) * 5.0))
        noise = noise_amp * np.random.normal(0.0, 1.0)
        
        return result + noise