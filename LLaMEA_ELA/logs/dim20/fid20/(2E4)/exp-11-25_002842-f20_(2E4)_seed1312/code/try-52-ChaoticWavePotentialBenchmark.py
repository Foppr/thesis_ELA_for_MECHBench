import numpy as np

class ChaoticWavePotentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Exponential decay components with varying rates
        exp_decay = np.sum(np.exp(-0.5 * x**2) * np.sin(3 * x) + np.exp(-0.3 * x**2) * np.cos(4 * x))
        
        # Trigonometric wave interference patterns with frequency modulation
        wave_interference = 0.8 * np.sum(np.sin(2 * x + np.sin(x)) * np.cos(3 * x + np.cos(x)))
        
        # Asymmetric polynomial potentials to create directional bias
        asym_poly = 0.3 * np.sum(x**3 * np.abs(x) + 0.5 * x**4 * np.sign(x))
        
        # Chaotic logistic map inspired cross-terms for increased complexity
        logistic_cross = 0.2 * np.sum((np.sin(x[:-1]) * np.cos(x[1:])) * (1 - x[:-1]**2) + 
                                     (np.cos(x[:-1]) * np.sin(x[1:])) * (1 - x[1:]**2))
        
        # Multi-scale sinusoidal modulation with varying amplitudes
        multi_scale = 0.4 * np.sum(np.sin(5 * x) * np.exp(-0.1 * np.abs(x)) + 
                                  np.cos(7 * x) * np.exp(-0.05 * np.abs(x)))
        
        # Gaussian radial basis with non-uniform spacing
        gaussian_basis = 0.25 * np.sum(np.exp(-0.5 * (x - np.linspace(-3, 3, self.dim))**2))
        
        # Hyperbolic tangent potential for sharp curvature regions
        tanh_potential = 0.35 * np.sum(np.tanh(2 * x)**2 + np.tanh(0.5 * x)**3)
        
        # Logarithmic spiral component for rotational invariance breaking
        log_spiral = 0.15 * np.sum(np.log(1 + np.abs(x)) * np.sin(np.log(np.abs(x) + 1)))
        
        # Cubic spline inspired interaction terms with non-linear coupling
        cubic_interaction = 0.2 * np.sum((x[:-1]**2 + x[1:]**2) * (x[:-1] - x[1:])**3)
        
        # Fractional Brownian motion inspired roughness term
        fbm_roughness = 0.1 * np.sum(np.abs(x[:-1] - x[1:])**(0.7) + np.abs(x[1:] - x[:-1])**(0.7))
        
        return exp_decay + wave_interference + asym_poly + logistic_cross + multi_scale + gaussian_basis + tanh_potential + log_spiral + cubic_interaction + fbm_roughness