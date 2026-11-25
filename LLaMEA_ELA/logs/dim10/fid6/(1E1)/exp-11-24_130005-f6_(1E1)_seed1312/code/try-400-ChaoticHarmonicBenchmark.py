import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base harmonic oscillation component with chaotic modulation
        harmonic = 0.0
        for i in range(self.dim):
            # Chaotic frequency modulation using logistic map-like behavior
            freq = 2.0 + 1.5 * np.sin(x_scaled[i] * 3.0) + 0.8 * np.cos(x_scaled[i] * 2.5)
            amp = 1.0 + 0.3 * np.sin(x_scaled[i] * 4.0)
            harmonic += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.5)
        
        # Hyper-elastic potential with embedded saddle points
        elastic = 0.0
        for i in range(self.dim):
            # Multi-well potential with varying depth and width
            well1 = (x_scaled[i] - 0.3)**2 * (x_scaled[i] + 0.3)**2
            well2 = (x_scaled[i] - 0.7)**2 * (x_scaled[i] + 0.7)**2
            well3 = x_scaled[i]**4 - 0.5 * x_scaled[i]**2
            elastic += 0.5 * (well1 + well2 + well3)
        
        # Multi-scale interaction terms with cross-dimensional coupling
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Cross-dimensional harmonic coupling with varying phase shifts
                phase_shift = np.sin(i * 0.5) * np.cos(j * 0.3)
                interaction += np.sin(x_scaled[i] + x_scaled[j] + phase_shift) * \
                              np.cos(x_scaled[i] - x_scaled[j] + phase_shift) * \
                              np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Chaotic saddle point landscape with exponential decay
        saddle = 0.0
        for i in range(self.dim):
            # Saddle point configuration with varying curvature
            curv1 = np.exp(-x_scaled[i]**2) * np.sin(5.0 * x_scaled[i])
            curv2 = np.exp(-(x_scaled[i] - 0.5)**2) * np.cos(3.0 * x_scaled[i])
            saddle += curv1 * curv2
        
        # Fractal-like self-similarity with recursive scaling
        fractal = 0.0
        for scale in [1, 2, 3, 4]:
            for i in range(self.dim):
                # Recursive pattern with diminishing amplitude
                fractal += (1.0 / scale) * np.sin(scale * x_scaled[i]) * \
                          np.cos(scale * x_scaled[i] * 0.7) * \
                          np.exp(-scale * np.abs(x_scaled[i]))
        
        # Sharp ridge and valley transitions
        transition = 0.0
        for i in range(self.dim):
            # Hyperbolic tangent transitions for sharp boundaries
            ridge = np.tanh(10.0 * (x_scaled[i] - 0.2)) + np.tanh(10.0 * (x_scaled[i] + 0.2))
            valley = np.tanh(15.0 * x_scaled[i])
            transition += ridge**2 + valley**2
        
        # Combined landscape with carefully balanced components
        return 1.2 * harmonic + 0.8 * elastic + 0.6 * interaction + 0.9 * saddle + 0.7 * fractal + 0.5 * transition