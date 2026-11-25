import numpy as np

class PolynomialTrigonometricRBF:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with orthogonal polynomials
        poly_chaos = np.sum((x**4 + 0.7 * x**3 - 0.5 * x**2 + 1.2 * x + 0.8) * np.cos(0.5 * x))
        
        # Trigonometric wave interference pattern with multiple frequencies
        trig_wave = np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) + 0.5 * np.sin(5.0 * x) * np.cos(7.0 * x))
        
        # Radial basis function component with varying widths and centers
        rbf_term = 0.0
        centers = np.linspace(-4.0, 4.0, 12)
        for center in centers:
            rbf_term += np.exp(-0.5 * np.sum((x - center)**2) / 1.0**2)
        
        # High-frequency oscillation component to increase complexity
        high_freq = np.sum(np.sin(25.0 * x) + 0.3 * np.cos(30.0 * x))
        
        # Cross-term interaction with nonlinear coupling
        cross_term = np.sum((x[:-1] ** 1.5) * (x[1:] ** 1.3) * np.sin(x[:-1] + x[1:]))
        
        # Gaussian modulation for localized structure
        gauss_mod = np.sum(np.exp(-0.2 * x**2) * np.sin(4.0 * x))
        
        # Sine-wave distortion component with varying amplitudes
        sine_distort = np.sum(0.8 * np.sin(1.5 * x) + 0.4 * np.sin(6.0 * x) + 0.2 * np.sin(12.0 * x))
        
        # Combine all terms with optimized weights
        return 0.30 * poly_chaos + 0.25 * trig_wave + 0.20 * rbf_term + 0.10 * high_freq + 0.08 * cross_term + 0.05 * gauss_mod + 0.02 * sine_distort + 1.5