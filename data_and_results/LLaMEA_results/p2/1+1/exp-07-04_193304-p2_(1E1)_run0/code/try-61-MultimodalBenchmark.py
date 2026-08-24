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
        f2 = 5.0 * np.sum(np.cos(60 * np.pi * x_norm))
        
        # Additional quartic term with modified coefficient
        f3 = 0.5 * np.sum(x_norm**4)
        
        # Cross-term interaction to increase conditioning
        f4 = 1.0 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Additional quadratic interaction term
        f5 = 0.6 * np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Fifth power term for added complexity
        f6 = 0.3 * np.sum(np.abs(x_norm)**5)
        
        # Additional sine term for increased multimodality
        f7 = 1.1 * np.sum(np.sin(50 * np.pi * x_norm))
        
        # Sixth power term for enhanced curvature
        f8 = 0.2 * np.sum(x_norm**6)
        
        # Additional cosine term with different frequency for more structure
        f9 = 0.5 * np.sum(np.cos(40 * np.pi * x_norm))
        
        # Modified quadratic interaction with higher weight
        f10 = 0.6 * np.sum((x_norm[:-2] - x_norm[2:])**2)
        
        # Additional higher-order interaction term
        f11 = 0.3 * np.sum((x_norm[:-3] - x_norm[3:])**2)
        
        # Increased penalty for large values
        f12 = 0.3 * np.sum(np.abs(x_norm)**7)
        
        # New Gaussian-like penalty term with modified decay rate and amplitude
        f13 = 0.3 * np.sum(np.exp(-5.0 * x_norm**2))
        
        # Chaotic interaction term using sine and cosine combinations
        f14 = 0.4 * np.sum(np.sin(60 * np.pi * x_norm) * np.cos(40 * np.pi * x_norm))
        
        # High-frequency oscillation component
        f15 = 0.3 * np.sum(np.sin(120 * x_norm))
        
        # Exponential decay with modified base
        f16 = 0.25 * np.sum(np.exp(-7.0 * np.abs(x_norm)))
        
        # Cubic interaction term
        f17 = 0.25 * np.sum(x_norm**3)
        
        # Mixed power and trigonometric term
        f18 = 0.2 * np.sum(np.sin(30 * x_norm**2))
        
        # Additional chaotic sine-cosine interaction
        f19 = 0.3 * np.sum(np.sin(45 * np.pi * x_norm) * np.cos(55 * np.pi * x_norm))
        
        # Additional exponential term with negative base
        f20 = 0.2 * np.sum(np.exp(-3.0 * x_norm**2))
        
        # Increased penalty for extreme values
        f21 = 0.2 * np.sum(np.abs(x_norm)**8)
        
        # Enhanced cubic term with different coefficient
        f22 = 0.25 * np.sum(x_norm**5)
        
        # Additional high-frequency cosine term
        f23 = 0.35 * np.sum(np.cos(70 * np.pi * x_norm))
        
        # Complex interaction with 4-dimensional jumps
        f24 = 0.25 * np.sum((x_norm[:-4] - x_norm[4:])**2)
        
        # Additional chaotic sine-cosine interaction with different frequencies
        f25 = 0.25 * np.sum(np.sin(50 * np.pi * x_norm) * np.cos(60 * np.pi * x_norm))
        
        # Additional exponential term with modified base
        f26 = 0.15 * np.sum(np.exp(-2.0 * x_norm**2))
        
        # Increased penalty for very large values
        f27 = 0.1 * np.sum(np.abs(x_norm)**9)
        
        # Additional high-order power term
        f28 = 0.1 * np.sum(x_norm**8)
        
        # Additional chaotic sine term with different frequency
        f29 = 0.2 * np.sum(np.sin(70 * x_norm))
        
        # Additional interaction term with 5-dimensional jumps
        f30 = 0.2 * np.sum((x_norm[:-5] - x_norm[5:])**2)
        
        # Additional chaotic sine-cosine interaction with even higher frequencies
        f31 = 0.25 * np.sum(np.sin(70 * np.pi * x_norm) * np.cos(80 * np.pi * x_norm))
        
        # Additional exponential term with even higher decay rate
        f32 = 0.15 * np.sum(np.exp(-8.0 * x_norm**2))
        
        # Additional high-frequency sine term
        f33 = 0.2 * np.sum(np.sin(80 * x_norm))
        
        # Additional power term with higher order
        f34 = 0.06 * np.sum(x_norm**9)
        
        # Additional interaction with 6-dimensional jumps
        f35 = 0.15 * np.sum((x_norm[:-6] - x_norm[6:])**2)
        
        # Additional chaotic interaction with 3-dimensional jumps
        f36 = 0.15 * np.sum((x_norm[:-3] - x_norm[3:])**2)
        
        # Additional exponential term with very high decay rate
        f37 = 0.1 * np.sum(np.exp(-9.0 * x_norm**2))
        
        # Additional sine term with very high frequency
        f38 = 0.15 * np.sum(np.sin(90 * x_norm))
        
        # Additional cosine term with very high frequency
        f39 = 0.2 * np.sum(np.cos(90 * np.pi * x_norm))
        
        # Additional power term with even higher order
        f40 = 0.04 * np.sum(x_norm**10)
        
        # Additional chaotic sine-cosine interaction with extremely high frequencies
        f41 = 0.3 * np.sum(np.sin(80 * np.pi * x_norm) * np.cos(90 * np.pi * x_norm))
        
        # Additional exponential term with extremely high decay rate
        f42 = 0.18 * np.sum(np.exp(-10.0 * x_norm**2))
        
        # Additional high-frequency sine term with extreme frequency
        f43 = 0.25 * np.sum(np.sin(100 * x_norm))
        
        # Additional power term with extremely high order
        f44 = 0.05 * np.sum(x_norm**11)
        
        # Additional interaction with 7-dimensional jumps
        f45 = 0.12 * np.sum((x_norm[:-7] - x_norm[7:])**2)
        
        # Additional chaotic interaction with 2-dimensional jumps
        f46 = 0.1 * np.sum((x_norm[:-2] - x_norm[2:])**2)
        
        # Additional exponential term with extremely high base
        f47 = 0.22 * np.sum(np.exp(-11.0 * x_norm**2))
        
        # Additional sine term with extremely high frequency
        f48 = 0.2 * np.sum(np.sin(110 * x_norm))
        
        # Additional cosine term with extremely high frequency
        f49 = 0.25 * np.sum(np.cos(100 * np.pi * x_norm))
        
        # Additional power term with extremely high order
        f50 = 0.03 * np.sum(x_norm**12)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18 + f19 + f20 + f21 + f22 + f23 + f24 + f25 + f26 + f27 + f28 + f29 + f30 + f31 + f32 + f33 + f34 + f35 + f36 + f37 + f38 + f39 + f40 + f41 + f42 + f43 + f44 + f45 + f46 + f47 + f48 + f49 + f50