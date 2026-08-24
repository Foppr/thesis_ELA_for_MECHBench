import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Sum of squares term
        f1 = np.sum(x_norm**2)
        
        # Multimodal term with increased frequency and amplitude
        f2 = 3.2 * np.sum(np.cos(55 * np.pi * x_norm))
        
        # Additional quartic term with modified coefficient
        f3 = 0.45 * np.sum(x_norm**4)
        
        # Cross-term interaction to increase conditioning
        f4 = 0.85 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Additional quadratic interaction term
        f5 = 0.55 * np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Fifth power term for added complexity
        f6 = 0.22 * np.sum(np.abs(x_norm)**5)
        
        # Additional sine term for increased multimodality
        f7 = 0.95 * np.sum(np.sin(45 * np.pi * x_norm))
        
        # Sixth power term for enhanced curvature
        f8 = 0.16 * np.sum(x_norm**6)
        
        # Additional cosine term with different frequency for more structure
        f9 = 0.42 * np.sum(np.cos(35 * np.pi * x_norm))
        
        # Modified quadratic interaction with higher weight
        f10 = 0.55 * np.sum((x_norm[:-2] - x_norm[2:])**2)
        
        # Additional higher-order interaction term
        f11 = 0.26 * np.sum((x_norm[:-3] - x_norm[3:])**2)
        
        # Increased penalty for large values
        f12 = 0.22 * np.sum(np.abs(x_norm)**7)
        
        # New Gaussian-like penalty term with modified decay rate and amplitude
        f13 = 0.26 * np.sum(np.exp(-4.2 * x_norm**2))
        
        # Chaotic interaction term using sine and cosine combinations
        f14 = 0.37 * np.sum(np.sin(55 * np.pi * x_norm) * np.cos(35 * np.pi * x_norm))
        
        # High-frequency oscillation component
        f15 = 0.26 * np.sum(np.sin(105 * x_norm))
        
        # Exponential decay with modified base
        f16 = 0.21 * np.sum(np.exp(-6.2 * np.abs(x_norm)))
        
        # Cubic interaction term
        f17 = 0.21 * np.sum(x_norm**3)
        
        # Mixed power and trigonometric term
        f18 = 0.16 * np.sum(np.sin(27 * x_norm**2))
        
        # Additional chaotic sine-cosine interaction
        f19 = 0.26 * np.sum(np.sin(37 * np.pi * x_norm) * np.cos(47 * np.pi * x_norm))
        
        # Additional exponential term with negative base
        f20 = 0.16 * np.sum(np.exp(-2.7 * x_norm**2))
        
        # Increased penalty for extreme values
        f21 = 0.16 * np.sum(np.abs(x_norm)**8)
        
        # Enhanced cubic term with different coefficient
        f22 = 0.21 * np.sum(x_norm**5)
        
        # Additional high-frequency cosine term
        f23 = 0.31 * np.sum(np.cos(65 * np.pi * x_norm))
        
        # Complex interaction with 4-dimensional jumps
        f24 = 0.21 * np.sum((x_norm[:-4] - x_norm[4:])**2)
        
        # Additional chaotic sine-cosine interaction with different frequencies
        f25 = 0.21 * np.sum(np.sin(42 * np.pi * x_norm) * np.cos(52 * np.pi * x_norm))
        
        # Additional exponential term with modified base
        f26 = 0.11 * np.sum(np.exp(-1.7 * x_norm**2))
        
        # Increased penalty for very large values
        f27 = 0.09 * np.sum(np.abs(x_norm)**9)
        
        # Additional high-order power term
        f28 = 0.09 * np.sum(x_norm**8)
        
        # Additional chaotic sine term with different frequency
        f29 = 0.16 * np.sum(np.sin(65 * x_norm))
        
        # Additional interaction term with 5-dimensional jumps
        f30 = 0.16 * np.sum((x_norm[:-5] - x_norm[5:])**2)
        
        # Additional chaotic sine-cosine interaction with even higher frequencies
        f31 = 0.21 * np.sum(np.sin(65 * np.pi * x_norm) * np.cos(75 * np.pi * x_norm))
        
        # Additional exponential term with even higher decay rate
        f32 = 0.13 * np.sum(np.exp(-7.2 * x_norm**2))
        
        # Additional high-frequency sine term
        f33 = 0.19 * np.sum(np.sin(75 * x_norm))
        
        # Additional power term with higher order
        f34 = 0.055 * np.sum(x_norm**9)
        
        # Additional interaction with 6-dimensional jumps
        f35 = 0.11 * np.sum((x_norm[:-6] - x_norm[6:])**2)
        
        # Additional chaotic interaction with 3-dimensional jumps
        f36 = 0.13 * np.sum((x_norm[:-3] - x_norm[3:])**2)
        
        # Additional exponential term with very high decay rate
        f37 = 0.09 * np.sum(np.exp(-8.2 * x_norm**2))
        
        # Additional sine term with very high frequency
        f38 = 0.11 * np.sum(np.sin(85 * x_norm))
        
        # Additional cosine term with very high frequency
        f39 = 0.16 * np.sum(np.cos(85 * np.pi * x_norm))
        
        # Additional power term with even higher order
        f40 = 0.035 * np.sum(x_norm**10)
        
        # New chaotic interaction term with 7-dimensional jumps
        f41 = 0.08 * np.sum((x_norm[:-7] - x_norm[7:])**2)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18 + f19 + f20 + f21 + f22 + f23 + f24 + f25 + f26 + f27 + f28 + f29 + f30 + f31 + f32 + f33 + f34 + f35 + f36 + f37 + f38 + f39 + f40 + f41