import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Enhanced polynomial chaos expansion with Chebyshev polynomials and higher degrees
        poly_chaos = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Chebyshev polynomial terms up to degree 8
            t1, t2, t3, t4, t5, t6, t7, t8 = (xi, 
                                            2*xi**2 - 1,
                                            4*xi**3 - 3*xi,
                                            8*xi**4 - 8*xi**2 + 1,
                                            16*xi**5 - 20*xi**3 + 5*xi,
                                            32*xi**6 - 48*xi**4 + 18*xi**2 - 1,
                                            64*xi**7 - 112*xi**5 + 56*xi**3 - 7*xi,
                                            128*xi**8 - 256*xi**6 + 160*xi**4 - 32*xi**2 + 1)
            poly_chaos += (t1 + 0.4*t2 + 0.2*t3 + 0.1*t4 + 0.05*t5 + 0.02*t6 + 0.01*t7 + 0.005*t8) * np.cos(3*np.pi*i)
        
        # Extended radial basis function with multi-scale Gaussian kernels and varying widths
        rbf = 0
        centers = np.linspace(-1, 1, min(12, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                center = centers[i]
                width = 0.3 + 0.7 * np.sin(i * np.pi / self.dim) * np.cos(2*i)
                rbf += np.exp(-0.5 * ((x_norm[i] - center) / width)**2) * (1 + 0.5 * np.sin(9*i) * np.cos(5*i))
        
        # Stronger gradient asymmetry with directional bias and sine modulation
        grad_asym = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Enhanced directional bias that increases with dimension index
            bias = 1.5 + 0.8 * np.sin(i * np.pi / self.dim) * np.cos(4*i)
            grad_asym += (xi**4 + 0.6*xi**3 - 0.4*xi**2 + 0.1*xi) * bias * np.sin(5*xi)
        
        # Enhanced periodic boundary effect with multiple frequencies
        periodic = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple periodic components with different frequencies and amplitudes
            periodic += (np.sin(3*np.pi*xi) + 0.7*np.sin(6*np.pi*xi) + 
                        0.5*np.sin(9*np.pi*xi) + 0.3*np.sin(12*np.pi*xi)) * np.cos(4*i)
        
        # Extended cross-dimensional coupling with sine interaction terms
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Sine coupling with varying strength and phase shifts
                coupling_strength = 0.7 + 0.3 * np.sin((i+j) * np.pi / self.dim) * np.cos(2*(i-j))
                cross_coupling += coupling_strength * np.sin(np.pi * (x_norm[i] + x_norm[j]))
        
        # High-frequency oscillatory component with chaotic modulation
        freq_osc = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Enhanced chaotic modulation using multiple logistic map-like behaviors
            chaotic_factor = 1.0 + 0.5 * np.sin(17*xi) * np.cos(19*xi) * np.sin(23*xi)
            freq_osc += (xi**3 * np.sin(25*xi) * np.cos(20*xi)) * chaotic_factor
        
        # Additional high-frequency component with fractal-like behavior
        fractal = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Fractal-like modulation using multiple sine waves
            fractal += (np.sin(30*xi) + 0.5*np.sin(60*xi) + 0.2*np.sin(90*xi)) * np.cos(7*i)
        
        # Combine all terms with adaptive weights
        result = 2.2 * poly_chaos + 1.8 * rbf + 1.6 * grad_asym + 1.2 * periodic + \
                1.4 * cross_coupling + 1.1 * freq_osc + 0.9 * fractal
        
        # Add stronger controlled noise for robustness
        noise = np.random.normal(0, 0.01)
        
        return result + noise