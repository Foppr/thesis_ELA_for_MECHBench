import numpy as np

class ChaoticTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Trigonometric chaos component with logistic map-like behavior
        trig_chaos = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Chaotic modulation using sine and cosine with varying frequencies
            chaotic_freq = 2 + 3 * np.sin(i * np.pi / self.dim)
            trig_chaos += (np.sin(chaotic_freq * xi) * np.cos(2 * chaotic_freq * xi) + 
                          0.5 * np.sin(3 * chaotic_freq * xi)) * np.cos(i)
        
        # Radial basis function with multiquadric kernels and varying centers
        rbf = 0
        centers = np.linspace(-1, 1, min(6, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                center = centers[i]
                # Multiquadric RBF with dimension-dependent width
                width = 0.3 + 0.4 * np.cos(i * np.pi / self.dim)
                rbf += np.sqrt((x_norm[i] - center)**2 + width**2) * (1 + 0.2 * np.sin(5*i))
        
        # Gradient asymmetry with hyperbolic tangent modulation
        grad_asym = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Asymmetric gradient with hyperbolic tangent
            asym_factor = 1.0 + 0.3 * np.tanh(xi * (i + 1))
            grad_asym += (xi**4 - 0.5*xi**2) * asym_factor * np.sin(3*xi)
        
        # Periodic boundary effect with wavelet-like components
        periodic = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Wavelet-like periodic terms with varying scales
            scale = 1.0 + 0.5 * np.cos(i * np.pi / self.dim)
            periodic += (np.sin(scale * xi) + 0.3 * np.cos(2 * scale * xi)) * np.sin(i)
        
        # Cross-dimensional coupling with sigmoid interaction terms - modified coupling strengths
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Sigmoid coupling with varying strength - increased variation
                coupling_strength = 0.9 + 0.6 * np.sin((i+j) * np.pi / self.dim)
                cross_coupling += coupling_strength * (1 / (1 + np.exp(-(x_norm[i] + x_norm[j]))))
        
        # High-frequency oscillatory component with fractal-like modulation
        freq_osc = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Fractal-like modulation using multiple sine waves
            fractal_mod = 1.0 + 0.2 * (np.sin(7*xi) + np.cos(11*xi) + np.sin(13*xi))
            freq_osc += (xi**3 * np.sin(15*xi)) * fractal_mod
        
        # Add polynomial cross-terms for increased conditioning
        poly_cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_cross += 0.1 * (x_norm[i]**2) * (x_norm[j]**3) * np.cos(i*j)
        
        # Combine all terms with modified weights
        result = 2.0 * trig_chaos + 1.3 * rbf + 1.1 * grad_asym + 0.9 * periodic + \
                1.5 * cross_coupling + 0.8 * freq_osc + 0.3 * poly_cross
        
        # Add controlled noise for robustness
        noise = np.random.normal(0, 0.003)
        
        return result + noise