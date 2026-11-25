import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Polynomial chaos expansion with Hermite polynomials and mixed degrees
        poly_chaos = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Hermite polynomial terms up to degree 6
            h1, h2, h3, h4, h5, h6 = (xi, 
                                    2*xi**2 - 1,
                                    4*xi**3 - 3*xi,
                                    8*xi**4 - 8*xi**2 + 1,
                                    16*xi**5 - 20*xi**3 + 5*xi,
                                    32*xi**6 - 48*xi**4 + 18*xi**2 - 1)
            poly_chaos += (h1 + 0.5*h2 + 0.3*h3 + 0.1*h4 + 0.05*h5 + 0.01*h6) * np.cos(2*np.pi*i)
        
        # Radial basis function with Gaussian kernels and varying widths
        rbf = 0
        centers = np.linspace(-1, 1, min(8, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                center = centers[i]
                width = 0.5 + 0.5 * np.sin(i * np.pi / self.dim)
                rbf += np.exp(-0.5 * ((x_norm[i] - center) / width)**2) * (1 + 0.3 * np.sin(7*i))
        
        # Gradient asymmetry with directional bias and sine modulation
        grad_asym = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Directional bias that increases with dimension index
            bias = 1.0 + 0.5 * np.sin(i * np.pi / self.dim) * np.cos(3*i)
            grad_asym += (xi**3 + 0.5*xi**2 - 0.3*xi) * bias * np.sin(4*xi)
        
        # Periodic boundary effect with multiple frequencies
        periodic = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple periodic components with different frequencies and amplitudes
            periodic += (np.sin(2*np.pi*xi) + 0.5*np.sin(4*np.pi*xi) + 
                        0.3*np.sin(6*np.pi*xi)) * np.cos(3*i)
        
        # Cross-dimensional coupling with cosine interaction terms
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cosine coupling with varying strength
                coupling_strength = 0.5 + 0.5 * np.cos((i+j) * np.pi / self.dim)
                cross_coupling += coupling_strength * np.cos(np.pi * (x_norm[i] + x_norm[j]))
        
        # High-frequency oscillatory component with chaotic modulation
        freq_osc = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Chaotic modulation using logistic map-like behavior
            chaotic_factor = 1.0 + 0.3 * np.sin(13*xi) * np.cos(17*xi)
            freq_osc += (xi**2 * np.sin(20*xi) * np.cos(15*xi)) * chaotic_factor
        
        # Combine all terms with adaptive weights
        result = 1.8 * poly_chaos + 1.5 * rbf + 1.2 * grad_asym + 0.8 * periodic + \
                1.0 * cross_coupling + 0.9 * freq_osc
        
        # Add controlled noise for robustness
        noise = np.random.normal(0, 0.005)
        
        return result + noise