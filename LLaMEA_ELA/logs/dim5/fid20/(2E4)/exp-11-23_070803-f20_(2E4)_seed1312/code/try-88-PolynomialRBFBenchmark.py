import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Enhanced polynomial chaos expansion with Hermite polynomials and mixed degrees
        poly_chaos = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Higher degree Hermite polynomial terms up to degree 8
            h1, h2, h3, h4, h5, h6, h7, h8 = (xi, 
                                            2*xi**2 - 1,
                                            4*xi**3 - 3*xi,
                                            8*xi**4 - 8*xi**2 + 1,
                                            16*xi**5 - 20*xi**3 + 5*xi,
                                            32*xi**6 - 48*xi**4 + 18*xi**2 - 1,
                                            64*xi**7 - 112*xi**5 + 56*xi**3 - 7*xi,
                                            128*xi**8 - 256*xi**6 + 160*xi**4 - 32*xi**2 + 1)
            # Add chaotic modulation to polynomial coefficients
            coeff_mod = 1.0 + 0.2 * np.sin(17*i) * np.cos(13*i)
            poly_chaos += (h1 + 0.5*h2 + 0.3*h3 + 0.1*h4 + 0.05*h5 + 0.01*h6 + 0.005*h7 + 0.001*h8) * coeff_mod * np.cos(2*np.pi*i)
        
        # Enhanced radial basis function with Gaussian kernels and varying widths
        rbf = 0
        centers = np.linspace(-1, 1, min(12, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                center = centers[i]
                width = 0.3 + 0.7 * np.sin(i * np.pi / self.dim) * np.cos(5*i)
                # Add chaotic modulation to kernel widths
                width_mod = 1.0 + 0.1 * np.sin(19*i) * np.cos(11*i)
                rbf += np.exp(-0.5 * ((x_norm[i] - center) / (width * width_mod))**2) * (1 + 0.4 * np.sin(7*i))
        
        # Enhanced gradient asymmetry with directional bias and sine modulation
        grad_asym = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Directional bias that increases with dimension index and has chaotic modulation
            bias = 1.0 + 0.7 * np.sin(i * np.pi / self.dim) * np.cos(3*i) * np.sin(13*i)
            grad_asym += (xi**4 + 0.6*xi**3 - 0.4*xi**2 + 0.1*xi) * bias * np.sin(5*xi)
        
        # Enhanced periodic boundary effect with multiple frequencies
        periodic = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple periodic components with different frequencies and amplitudes, chaotic modulation
            freq_mod = 1.0 + 0.2 * np.sin(11*i) * np.cos(7*i)
            periodic += (np.sin(3*np.pi*xi) + 0.6*np.sin(6*np.pi*xi) + 
                        0.4*np.sin(9*np.pi*xi) + 0.2*np.sin(12*np.pi*xi)) * freq_mod * np.cos(5*i)
        
        # Enhanced cross-dimensional coupling with cosine interaction terms
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cosine coupling with varying strength and chaotic modulation
                coupling_strength = 0.6 + 0.4 * np.cos((i+j) * np.pi / self.dim) * np.sin(17*i)
                cross_coupling += coupling_strength * np.cos(np.pi * (x_norm[i] + x_norm[j])) * np.sin(13*(i+j))
        
        # Enhanced high-frequency oscillatory component with chaotic modulation
        freq_osc = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Chaotic modulation using logistic map-like behavior with higher frequency components
            chaotic_factor = 1.0 + 0.4 * np.sin(13*xi) * np.cos(17*xi) * np.sin(23*xi)
            freq_osc += (xi**3 * np.sin(25*xi) * np.cos(20*xi)) * chaotic_factor
        
        # Additional chaotic landscape components
        chaotic_comp = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Sine-cosine chaotic interaction
            chaotic_comp += (np.sin(37*xi) + np.cos(41*xi)) * np.sin(29*i) * np.cos(31*i)
        
        # Combine all terms with adaptive weights
        result = 2.0 * poly_chaos + 1.8 * rbf + 1.5 * grad_asym + 1.0 * periodic + \
                1.2 * cross_coupling + 1.1 * freq_osc + 0.7 * chaotic_comp
        
        # Add controlled noise for robustness
        noise = np.random.normal(0, 0.008)
        
        return result + noise