import numpy as np

class FractalSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute spherical harmonic coefficients
        self.sph_coeffs = np.random.randn(dim, 5)
        # Fractal Brownian motion parameters
        self.hurst = 0.3 + 0.4 * np.random.rand()
        self.fractal_dim = 2.0 + 1.0 * np.random.rand()
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Spherical harmonics component
        sph_harm = 0.0
        for i in range(self.dim):
            theta = np.arctan2(x_norm[i], x_norm[(i+1) % self.dim])
            phi = np.arccos(x_norm[i] / np.sqrt(np.sum(x_norm**2)))
            # Combine spherical harmonics with random coefficients
            for l in range(1, 4):
                for m in range(-l, l+1):
                    sph_harm += self.sph_coeffs[i, l-1] * np.real(
                        np.exp(1j * m * theta) * np.sqrt((2*l+1)/(4*np.pi)) * 
                        np.polynomial.legendre.legval(np.cos(phi), [0]*l + [1])
                    )
        
        # Fractal Brownian motion component
        fbm = 0.0
        for i in range(self.dim):
            # Generate fractal noise using midpoint displacement
            scale = 1.0
            for _ in range(5):
                fbm += scale * np.sin(x_norm[i] * (2**_))
                scale *= self.hurst
        
        # Adaptive noise component with varying intensity
        noise_amp = 0.5 + 0.5 * np.random.rand()
        adaptive_noise = np.sum(noise_amp * np.sin(10 * x_norm) * np.cos(15 * x_norm))
        
        # Multi-scale quadratic terms with directional coupling
        quad_terms = 0.0
        for i in range(self.dim):
            quad_terms += (x_norm[i]**2 + 0.1 * x_norm[i] * x_norm[(i+1) % self.dim])
            
        # Combined landscape with varying condition numbers
        return 0.3 * sph_harm + 0.4 * fbm + 0.2 * adaptive_noise + 0.1 * quad_terms + 2.0